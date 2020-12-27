library(plumber)
library(jsonlite)

# SET WORKING DIRECTORY SO THAT THE myModel.rds FILE CAN BE FOUND IN THE NEXT LINE

model <- readRDS('./myModel.rds')

#* @apiTitle Breast Cancer Diagnosis

#* @apiDescription Breast cancer diagnosis based on three relevant parameters. The prediction returns both predicted class and its class probability.

#* @param mean_concave_points ... enter the value as a number
#* @param worst_perimeter ...enter the value as a number
#* @param worst_concave_points ...enter the value as a number
#* @get /predict
function(worst_concave_points,worst_perimeter,mean_concave_points) {
  df <- data.frame("worst_concave_points" = as.numeric(worst_concave_points), 
                   "worst_perimeter" = as.numeric(worst_perimeter), 
                   "mean_concave_points" = as.numeric(mean_concave_points))
  
  prediction <- data.frame("Prediction" = predict(model, newdata = df, type = "response"), 
                           "Probability" = max(as.numeric(unlist(predict(model, newdata = df, type = "prob")))))
  
  response <- toJSON(prediction, dataframe = "columns")
  response
}

