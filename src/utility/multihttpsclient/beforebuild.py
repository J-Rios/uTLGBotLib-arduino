
# Import Build Environment 
Import("env")

# Get used PIO Framework (Doesn't exists in Native)
build_framework = []
if "PIOFRAMEWORK" in env:
    build_framework = env["PIOFRAMEWORK"]
    print("Build framework - {}".format(build_framework))

# Check build and ignore custom mbedtls for ESP32
if ("arduino" in build_framework) or ("espidf" in build_framework):
    print("ESP32 Build detected, ignoring multihttpsclient/mbedtls.")
    env.Replace(SRC_FILTER=["+<*>", "-<.git/>", "-<mbedtls/>"])
else:
    print("Generic Native Build detected, using multihttpsclient/mbedtls.")
