$url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

$username = "devnetuser"
$password = ConvertTo-SecureString 'Cisco123!' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ($username, $password)

$headers = @{'Accept' = 'application/json'}
#get token for login
$get_token = Invoke-RestMethod -Uri $url `
    -Method Post `
    -ContentType 'application/json' `
    -Credential $cred `
    -Headers $headers `
    -SkipCertificateCheck

$token = $get_token.Token
# Write-Output $token

$url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

$headers = @{
    'Accept' = 'application/json'
    'x-auth-token' = $token
}
#get list of connected devices
$get_network = Invoke-RestMethod -Uri $url `
    -Method get `
    -Authentication Basic `
    -Credential $cred `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck


foreach ($network in $get_network.response) {
    Write-Host "device-name:$($network.type)"
    Write-Host "device-ip:$($network.managementIpAddress)"
    "&" * 50
}