object StringProcessorFunc {
  def processStrings(strings: List[String]): List[String] = {
    // Используем метод filter для выбора строк длиной больше 3
    // Затем используем метод map для преобразования выбранных строк в верхний регистр
    strings.filter(_.length > 3).map(_.toUpperCase)
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
