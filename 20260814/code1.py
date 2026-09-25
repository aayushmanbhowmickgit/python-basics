#PROGRAM TO CALCULATE GST
a=input("enter customer's state:")
b=input("enter store's state:")
s=int(input("enter the selling price:"))
gst=int(input("enter the GST:"))
p=s+(s*gst/100)
print("TOTAL PRICE IS : ",p)
if a==b:
    cgstAmount=0
    sgstAmount=0
    igstAmount=((s*gst)/100)
else:
    cgstAmount=((s*(gst/2))/100)
    sgstAmount=((s*(gst/2))/100)
    igstAmount=0 
print(f"CGST: {cgstAmount}")
print(f"SGST: {sgstAmount}")
print(f"IGST: {igstAmount}")