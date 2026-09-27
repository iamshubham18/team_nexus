import serial

# Configured for COM4
arduino_port = "COM4"
baud_rate = 9600

print(f"Connecting to Arduino on {arduino_port}...")
try:
  ser = serial.Serial(arduino_port, baud_rate, timeout=1)
  print(
      "Connected successfully! Listening for multi-hazard sensor telemetry..."
  )

  while True:
    if ser.in_waiting > 0:
      raw_data = ser.readline().decode("utf-8").strip()

      if raw_data:
        # Split CSV values: [Distance, Temp, Humidity, Flame, Vibration]
        values = raw_data.split(",")

        if len(values) >= 5:
          distance = float(values[0])
          temperature = float(values[1])
          humidity = float(values[2])
          flame_status = int(values[3])
          vibration_status = int(values[4])

          # --- PRINT LIVE TELEMETRY ---
          print(
              f"Distance: {distance} cm | Temp: {temperature} °C | Hum:"
              f" {humidity}% | Flame: {flame_status} | Vibration Hazard:"
              f" {vibration_status}"
          )

          # --- INSERT YOUR AI DASHBOARD LOGIC HERE ---
          # Pass these variables directly into your AI prediction model:
          # ai_prediction_result = run_ai_model(distance, temperature, humidity, flame_status, vibration_status)

except Exception as e:
  print(f"Error connecting to {arduino_port}: {e}")
  print(
      "Tip: Make sure the Arduino Serial Monitor is closed before running this"
      " script!"
  )