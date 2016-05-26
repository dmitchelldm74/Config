filename = "config.cfg"
import config
data = config.load(filename, VARS=True)
data["new"] = "value"
print(data)
