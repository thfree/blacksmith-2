выполняет shell команду
{command} [команда]
*/{command} TASKLIST /FI "IMAGENAME eq python.exe
бот покажет (windows) список запущенных процессов на python и занимаемаю ими память (ram)
*/{command} ps -o rss -p 12154
покажет (unix) сколько памяти хавает процесс с pid'ом 12154