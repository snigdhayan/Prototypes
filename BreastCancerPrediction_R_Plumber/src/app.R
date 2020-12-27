library(plumber)

# SET WORKING DIRECTORY SO THAT THE plumber.R FILE CAN BE FOUND IN THE NEXT LINE

pr <- plumb("./plumber.R")
pr$run(port=8000, swagger = TRUE)

# pr$run(host = '0.0.0.0', port=8000, swagger = TRUE) # make the service reachable from outside, if containerized