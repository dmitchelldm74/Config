filename = "config.cfg"
import config
data = config.load(filename, VARS=False)
data["new"] = "value"
config.dump(data, "dump~")
