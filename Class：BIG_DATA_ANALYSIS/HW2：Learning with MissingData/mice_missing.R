library("ggplot2")
library("mice")
data<-read.csv("C:\\Users\\kevin\\OneDrive\\桌面\\巨量\\HW2\\hw2_data\\data1\\test.csv",header=FALSE)
md.pattern(data)
data<-data[-c(9)]
mice.data <- mice(data,
                  maxit = 30,
                  m = 10,# max iteration
                  method = "cart", # 使用CART決策樹，進行遺漏值預測
                  seed = 188)  
mice.data$imp
stripplot(mice.data, col=c("grey",mdc(2)),pch=c(1,20))

IMP <- 0
for (i in 1:10) { IMP <- IMP + mice::complete(mice.data, i)}
mice.data <- IMP/10#

summary(mice.data)

write.table(mice.data,file="C:\\Users\\kevin\\OneDrive\\桌面\\巨量\\HW2\\hw2_data\\data1\\test_cart.csv",sep=",",row.names=F,,col.names=FALSE)

methods(mice)



###################
library("missMDA")
pca <- imputePCA(X = data, ncp = 2, scale = TRUE, method = c("Regularized","EM"))
ncp.pca <- estim_ncpPCA(data,method.cv="gcv")$ncp
pca <- imputePCA(data, ncp = ncp.pca)
data_pca <- pca$comp
write.table(data_pca,file="C:\\Users\\kevin\\OneDrive\\桌面\\巨量\\HW2\\hw2_data\\data1\\train_pca.csv",sep=",",row.names=F,,col.names=FALSE)

