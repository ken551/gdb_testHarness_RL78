#include "r_cg_macrodriver.h"
#include "r_cg_port.h"
#include "r_cg_userdefine.h"

void initPort4()
{
	P4 = 0x00;
}

void turnOnLed()
{
	return;
}

void toggleLed(uint8_t u1_id)
{
	if (u1_id == 0)
	{
		P4_bit.no2 = !P4_bit.no2;
	}
	else if (u1_id == 1)
	{
		P4_bit.no3 = !P4_bit.no3;
	}
}

uint8_t increment(uint8_t hoge)
{
	uint8_t fuga = hoge + 1;
	return fuga;
}

uint8_t returnTest(uint8_t hoge)
{
	hoge = increment(hoge);
	return hoge;
}

uint16_t returnBeef(uint8_t hoge)
{
	return 0xBEEF;
}
