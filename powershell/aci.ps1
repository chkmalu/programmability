$url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"
$payload = @{
    aaaUser = @{
        attributes = @{
            name = "admin"
            pwd  = "!v3G@!4@Y"
        }
    }
}

$headers = @{'Accept' = 'application/json' }

$response = Invoke-RestMethod -Uri $url `
    -Method post `
    -Body ($payload | ConvertTo-Json) `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -SessionVariable s
# Print token
Write-Host "Token: " -ForegroundColor Red -NoNewline
Write-Host $response.imdata.aaaLogin.attributes.token

$uri = "https://sandboxapicdc.cisco.com:443/api/node/class/fvTenant.json"

$tenants = Invoke-RestMethod -Uri $uri `
    -Method Get `
    -ContentType 'application/json' `
    -Headers $headers `
    -SkipCertificateCheck `
    -Websession $s
Write-Host "App: " -ForegroundColor Red 

$tenants | ConvertTo-Json | Write-Output