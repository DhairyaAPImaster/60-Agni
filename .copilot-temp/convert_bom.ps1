$csv = Import-Csv -Path 'd:\Dhairya\CAD\60%agni keyboard\Fabrication files\PCB\Agni keyboard BOM.csv' -Encoding Unicode
if ($csv.Count -eq 0) { exit 0 }
$h = $csv[0].psobject.properties.name
Write-Output ("| " + ($h -join " | ") + " |")
Write-Output ("| " + ($h | ForEach-Object { '---' } -join " | ") + " |")
foreach ($r in $csv) {
  $row = $h | ForEach-Object { $v = $r.$_; if ($v -eq $null) { '' } else { ($v -replace "`r",'') -replace "`n",' ' } }
  Write-Output ("| " + ($row -join " | ") + " |")
}
