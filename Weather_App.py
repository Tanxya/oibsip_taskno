import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    country = country_entry.get()
    api_key = "8311350fe03a8f2f00945fc0770a5593"  
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city},{country}"
    weather_label.config(text="Loading...")
    response = requests.get(url)
    weather_data = response.json()
    if "message" in weather_data:
        messagebox.showerror("Error", weather_data["message"])
    else:
        temperature = weather_data["current"]["temperature"]
        weather_desc = weather_data["current"]["weather_descriptions"][0]
        weather_text = f"City: {city}\n"
        weather_text += f"Temperature: {temperature}°C\n"
        weather_text += f"Description: {weather_desc}"
        weather_label.config(text=weather_text)

root = tk.Tk()
root.geometry("400x450")
root.configure(background="misty rose")
root.title("Weather App")
LABLE = tk.Label(root, bg="misty rose", text="Welcome to Weather App", font=("Helvetica", 15, "bold"), pady=10)
LABLE.place(x=75, y=8)
city_label = tk.Label(root, bg="misty rose", text="City:", bd=6,font=("Helvetica", 10, "bold"), pady=5)
city_label.place(x=90, y=62)
city_entry = tk.Entry(root, bd=5, width=15, font="Roboto 11")
city_entry.place(x=145, y=66)
country_label = tk.Label(root, bg="misty rose", text="Country:", bd=6,font=("Helvetica", 10, "bold"), pady=5)
country_label.place(x=80, y=122)
country_entry = tk.Entry(root, bd=5, width=15, font="Roboto 11")
country_entry.place(x=160, y=126)
get_weather_button = tk.Button(bg="deepskyblue", bd=5, text="Get Weather", width=10, command=get_weather, fg='black', activebackground="teal", font=("Helvetica", 12, "bold"))
get_weather_button.grid(row=2, column=0)
get_weather_button.place(x=145, y=180)
weather_frame = tk.Frame(root, bg='#80c1ff', bd=10)
weather_frame.place(relx=0.5, y=250, relwidth=0.75, relheight=0.3, anchor='n')
weather_label = tk.Label(weather_frame, font=("Helvetica", 10, "bold"), justify='left', bd=5)
weather_label.place(relwidth=1, relheight=1)
root.mainloop()