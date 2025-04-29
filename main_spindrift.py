def main():
  print("What is your name?")
  name = input()
  print(f"Would you like a Spindrift, {name}?")
  y_n = input()
  if lower(y_n) == "y":
    print("Good...")
  else:
    raise ValueError("Incorrect Option")

if __name__ == "__main__":
  main()
