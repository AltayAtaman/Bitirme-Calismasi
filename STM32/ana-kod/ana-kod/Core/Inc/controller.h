/*
 * controller.h
 *
 *  Created on: Jun 12, 2024
 *      Author: root
 */

#ifndef INC_CONTROLLER_H_
#define INC_CONTROLLER_H_

#define t 0
#define dt 0.01
#define Ae 0.99
#define damping_factor 0.2
#define theta_ref 10

// DC Motor Parametreleri
#define L 0.000113
#define R 0.199
#define J 0.0000023
#define b 0.000023873
#define ke 0.0000219
#define kt 0.0000217

// disli oranlari
#define N1 1
#define N2 70
#define N3 12.77
#define N4 8.25

// sonumleme ve yay katsayilari
#define k_spring 0.17
#define cM 0.022

//#define etaWG 0.3 // sonsuz disli verimi

float theta_0 = 0, theta_0_dot = 0;
float angPos = 0, angPos_prev = 0, angPos_prevprev = 0, angVel = 0;
float error = 0;
float voltage, torque = 0, torque_prev = 0;

// Disli kutleleri
float mM = 47.5 / 1000;
float mMSG = 17.5 / 1000;
float mWG = 100 / 1000;
float mDSP = 325 / 1000;
float mDSG = 89 / 1000;
float mSG = 180 / 1000;

// Disli yari-caplari
float rM = 5.25  / 1000;
float rMSG = 5.25 / 1000;
float rWG = 5.25 / 1000;
float rDSP = 25 / 1000;
float rDSG = 49.8 / 1000;
float rSG = 59.4 / 1000;

// Eylemsizlik hesaplari
float jM;
float jMSG;
float jWG;
float jDSP;
float jDSG;
float jSG;

float etaWG = 0.3; // sonsuz disli verimi

// Mekanik sistem - x katsayilari
float x1;
float x2;
float x3;
float x4;
float x5;
float x6;
float x7;

// Mekanik Sistem - y katsayilari
float y1;
float y2;
float y3;

// Merkezi farklar yontemi katsayilari
float fx_now;
float fx_pre;
float fx_fut;


void initializeController() {

	// Eylemsizlik hesaplari
	jM = J;
	jMSG = 0.5 * mMSG * (rMSG * rMSG);
	jWG = 0.5 * mWG * (rWG * rWG);
	jDSP = 0.5 * mDSP * (rDSP * rDSP);
	jDSG = 0.5 * mDSG * (rDSG * rDSG);
	jSG = 0.5 * mSG * (rSG * rSG);

	// Mekanik sistem - x katsayilari
	x1 = k_spring / (N1 * N2 * N3 * N4);
	x2 = jSG / ((N1 * N2 * N3 * N4) * (N1 * N2 * N3 * N4));
	x3 = jDSG / ((N1 * N2 * N3) * (N1 * N2 * N3));
	x4 = cM / (N1 * N2);
	x5 = jDSP / ((N1 * N2) * (N1 * N2));
	x6 = jWG / (N1 * N1);
	x7 = jM + jMSG;

	// Mekanik Sistem - y katsayilari
	y1 = x7 + x6 + (x5 + x3 + x2) / (etaWG);
	y2 = x4 / (etaWG);
	y3 = x1 / (etaWG);

	// Merkezi farklar yontemi katsayilari
	fx_now = (2 * y1 / (dt * dt)) - y3;
	fx_pre = (y2 / (2 * dt)) - (y1 / (dt *dt));
	fx_fut = (y1 / (dt * dt)) + (y2 / (2 * dt));
}

int controlMotor(float feedbackSpeed) {
	angPos_prev = feedbackSpeed;

	int error = theta_ref - angPos_prev;

	if (t == 0) {
		angPos = theta_0;
	}

	else {
		torque = damping_factor * fx_fut * (theta_ref - (((angPos_prev * fx_now) +
				(angPos_prevprev * fx_pre)) / fx_fut) - (Ae * error));

	    angPos = (angPos_prev * fx_now + angPos_prevprev * fx_pre + torque) / fx_fut;

	    angVel = (angPos - angPos_prevprev) / (2 * dt);

	    float current = torque / kt;
	    voltage = L * ((torque - torque_prev) / dt) + (R / kt) * torque + ke * ((angPos - angPos_prev) / dt);
	}

	angPos_prev = angPos;
	angPos_prevprev = angPos_prev;
	torque_prev = torque;

	return voltage;
}

int generatePWM() {
	__HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, pwm_duty * (htim3.Init.Period / 8));
}

#endif /* INC_CONTROLLER_H_ */
