# Lists the processes
$processes = Get-Process
# Gets process which has utilization more than 80%
$highCPUProcesses = $processes | Where-Object {$_.CPU -gt 80}
$logFile = "CPU_Usage_80.log" 
$currentDateTime = Get-Date -Format "yyyy-MM-dd_HH-mm-ss" # Current timestamp
# Populates the log file
$highCPUProcesses | Export-Csv $logFile -NoTypeInformation -Append -Force
