import math

count=0

#Prediction Steps
print "\nPrediction Steps"
print "----------------------------------------"

#	prediction for the mean
At= input("A: ")
Bt= input ("B: ")
ut_= input("Enter Prior Mean: ")
ut= input ("Enter Current Mean: ")

pMean= At*ut_+Bt*ut
print "Predicted Mean: ", pMean



#prediction for the covarivance

Et_=input("\nE(t-1): ")
Att=input("A(T/t): ")
Qt=input("Q(t): ")


pCo= At*Et_*Att+Qt
print "Predicted Convariance: ",pCo



while count==0:
	
	#Update Steps

	print "\nUpdate Steps"
	print "----------------------------------------"
	#Kalman gain Steps
	Ctt= input("C(T/t): ")
	Ct= input("C/(t): ")
	Rt=input ("Measurment Covariance: ")

	kGain=pCo*Ctt*math.pow((Ct*pCo*Ctt+Rt),(-1))

	print "Kalman Gain: ", kGain


	#Updated Mean Calculation Steps
	zt=input("\nActual Measurement: ")

	uMean=pMean+kGain*(zt-Ct*pMean)
	print "Updated Mean: ", uMean





	#Updated Standard Deviation Calculation Steps
	uCo=pCo-kGain*Ct*pCo
	print "\nUpdated Covariance: ", uCo

	#Prediction Steps
	print "\nPrediction Steps"
	print "----------------------------------------"

	#	prediction for the mean
	At= input("A: ")
	Bt= input ("B: ")
	#ut_= input("Enter Prior Mean: ")
	ut= input ("Enter Current Mean: ")

	pMean= At*uMean+Bt*ut
	print "Predicted Mean: ", pMean



	#prediction for the covarivance

	#Et_=input("E(t-1): ")
	Att=input("\nA(T/t): ")
	Qt=input("Q(t): ")


	pCo= At*uCo*Att+Qt
	print "Predicted Convariance: ",pCo



