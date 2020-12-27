library(caTools)
library(party)
              
# SET WORKING DIRECTORY SO THAT THE breast_cancer_dataset.csv FILE CAN BE FOUND IN THE NEXT LINE

data <- read.csv(file = './breast_cancer_dataset.csv', header = TRUE)
data$label <- as.factor(data$label)

# selected_features <- c("worst_concave_points","worst_perimeter","mean_concave_points","label")
# data <- data[selected_features]
# data <- data[names(data)!='label']

# prepare data for training and testing
set.seed(101) 
split_ratio = 0.7
sample = sample.split(data, SplitRatio = split_ratio)
data_train = subset(data, sample == TRUE)
data_test  = subset(data, sample == FALSE)

# A conditional inference tree model based on a very simple formula to reduce computational complexity
# start_time <- proc.time()
model <- ctree(label ~ worst_concave_points + worst_perimeter + mean_concave_points, data = data_train)
# model <- ctree(label ~ ., data = data_train)
# training_time <- proc.time() - start_time

saveRDS(model, file = './myModel.rds')

