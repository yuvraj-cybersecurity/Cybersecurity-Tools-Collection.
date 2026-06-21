from stegano import lsb

# Path set karein (apne phone ke storage se file dhoond kar path lein)
# Agar file wahi folder mein hai jahan code hai, toh sirf naam kaafi hai
input_image = "input.jpg" 
output_image = "secret_image.png"

# Message jo chhupana hai
message = "JEE Advanced Qualified: My secret mission!"

# 1. Message Hide karna
secret = lsb.hide(input_image, message)
secret.save(output_image)
print(f"Success! Message hidden in {output_image}")

# 2. Message Reveal (wapas nikalna)
reveal_msg = lsb.reveal(output_image)
print(f"Decoded Message: {reveal_msg}")
