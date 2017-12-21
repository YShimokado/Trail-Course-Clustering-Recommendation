#加工済みデータ読み込み
data <- read.csv('course_data_c_.csv')
#index列は削除
data <- data[,c(-1)]

#PCA
result <- prcomp(data,scale=T)
#グラフの描画
biplot(result,cex=0.8,xlim=c(-0.3,0.3),ylim=c(-0.3,0.3))
summary(result)

#元のデータに主成分を追加して書き出す
data_2 <- read.csv('course_data_c_.csv')
data_2<- transform(data_2,PC1=result$x[,1])
data_2<- transform(data_2,PC2=result$x[,2])
head(data_2)
write.csv(data_2,"course_data_c_PCA.csv")
