$url = "https://api.meraki.com/api/v0/organizations"
$headers = @{
    'Accept' = 'application/json'
    'X-Cisco-Meraki-API-Key' = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}
#get the list of organizations
$orgs = Invoke-RestMethod -Uri $url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers

#iterate to get id of a specific one
foreach ($org in $orgs) {
    if ($org.name -eq 'DevNet Sandbox') {
        $orgId = $org.id
    }
}
Write-Output "orgid = $($orgId)"
#get list of networks in the organization
$net_url = "https://api.meraki.com/api/v0/organizations/$($orgId)/networks"
$networks = Invoke-RestMethod -Uri $net_url `
    -Method get `
    -ContentType 'application/json' `
    -Headers $headers

#iterate over the list of network to get a specific one
foreach ($network in $networks) {
    if ($network.name -eq 'DNSMB4') {
        $netId = $network.id
    }
}
#get list of devices connect in the network
$devices_url = "https://api.meraki.com/api/v0/organizations/$($orgId)/networks/$($netId)/devices"
$devices `  = Invoke-RestMethod -uri $devices_url `
    -Method get `
    -ContentType 'applcation/json' `
    -Header $headers 

$devices | ConvertTo-Json | Write-Output