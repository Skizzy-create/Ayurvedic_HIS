from gradio_client import Client
import time

client = Client("https://skizzy-create-ona-ggml.hf.space/")

system_prompt = """Your name is MAITRI
Based on your illness or symptoms or the prompt given by the user, you will provide a remedy for the symptoms, dosage, composition of the medication, instructions on how to take it, precautions, and additional tips. Here's the format of my response:\n
- Herbs: [List of herbs included in the medication]\n
- How to make the medicine at home: [Instructions on how to prepare the medicine with precise measurements]\n
- How the medication will help: [Explanation of how the medication will aid in healing] \n
- Precautions: [Any precautions to be aware of while taking the medication]\n
- Tips: [Additional tips for managing the illness or enhancing the effectiveness of the medication]\n
Please note that while I strive to provide a human-like interaction, I won't use human gestures such as *winks*, smiling*, *nods*, *adjusts glasses*, etc. please answer in the most shortest format possible being to the point with the answer in a humanly manner.  User: I am suffering from sinus please provide me with ayurvedic solution.
now answer the user's query in the format given above.
"""
ans = "1"
#putting the below in a while loop so that when user says no the loop stops
while ans in ["1","2"]:
	#print the menu
	print ("""
	1.Enter the prompt
	2.Enter your Symptoms
	3.Exit/Quit
	""")
	ans=input("What would you like to do? ")

	if ans=="1":
		prompt_inp = str(input("Enter the prompt for chats:"))
		print("\nPrompt Entered")
		start = time.time()
		result = client.predict(
				prompt_inp,	# str in 'prompt' Textbox component
				api_name="/predict"
				)
		end = time.time()
		print(f"\n\tTime Taken: {end-start} seconds\n")
		print(result)

	elif ans=="2":
		prompt = str(input("Enter your Symptoms for advice:"))
		print("\nSymptoms Entered")
		prompt_inp_advice = system_prompt + " " + "###User : " + prompt + "Please suggest me some ayurvedic solution fo it. ###Assistant:"
		start = time.time()
		result = client.predict(
				prompt_inp_advice,	# str in 'prompt' Textbox component
				api_name="/predict"
				)
		end = time.time()
		print(f"\n\tTime Taken: {end-start} seconds\n")
		print(result)

	elif ans=="3":
		print("\n Goodbye")
		ans = None
	else:
		print("\n Not Valid Choice Try again")
    

