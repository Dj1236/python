print("tip su devi che tare vadhi paida")
total_bill=float(input("ketla no kharcho thayo lodav$"))
tip= int(input ("ketli tip devi aane 10,20,30,ke kai nai?"))
people= int(input("ketla jana bill dese hath ucho karo"))
#bill_with_tip = tip/100 * total_bill + total_bill
tip_as_percent = tip/100
total_tip_amount=total_bill*tip_as_percent
final_bill=(total_bill+total_tip_amount)/people #toh toy se divide hojayega
final_amount = round(final_bill,2)
print (f"total amount is {final_amount}")



