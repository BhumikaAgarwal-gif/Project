import qrcode

#Take user UPI ID as a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME=Amount&cu=CURRENCY&tr=MESSAGE

#you can modify given urls on you basis

google_pay_url = f'upi;//pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi;//pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
phonepe_url = f'upi;//pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create Qr codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr code to image file(optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
