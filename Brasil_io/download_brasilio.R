download_brasilio_table <- function(dataset, table_name){
  url <- sprintf("https://data.brasil.io/dataset/%s/%s.csv.gz", dataset, table_name)
  tmp <- tempfile()
  download.file(url, tmp)
  response <- read.csv(gzfile(tmp), encoding = "UTF-8")
  unlink(tmp)
  return(response)
}

# Passe o nome da tabela para a funcao, como "caso", "caso_full", "obito_cartorio":
data <- download_brasilio_table("covid19", "caso_full")