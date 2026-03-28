$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$OpencodeDir = if ($env:OPENCODE_DIR) { $env:OPENCODE_DIR } else { Join-Path $env:USERPROFILE ".config\opencode" }

Write-Host "Installing omo-awesome-subagents..."
Write-Host "  Source: $RepoRoot"
Write-Host "  Target: $OpencodeDir"

# Create target directories
New-Item -ItemType Directory -Force -Path "$OpencodeDir\agents" | Out-Null
New-Item -ItemType Directory -Force -Path "$OpencodeDir\skills" | Out-Null

# Copy agents (skip AGENTS.md meta file)
$copiedAgents = 0
Get-ChildItem "$RepoRoot\agents\*.md" | Where-Object { $_.Name -ne "AGENTS.md" } | ForEach-Object {
    Copy-Item $_.FullName "$OpencodeDir\agents\" -Force
    $copiedAgents++
}

# Copy skills (skip AGENTS.md meta file)
$copiedSkills = 0
Get-ChildItem "$RepoRoot\skills" -Directory | ForEach-Object {
    $skillName = $_.Name
    $skillFile = Join-Path $_.FullName "SKILL.md"
    if (Test-Path $skillFile) {
        New-Item -ItemType Directory -Force -Path "$OpencodeDir\skills\$skillName" | Out-Null
        Copy-Item $skillFile "$OpencodeDir\skills\$skillName\" -Force
        $copiedSkills++
    }
}

Write-Host ""
Write-Host "Done!"
Write-Host "  Installed $copiedAgents agents to $OpencodeDir\agents\"
Write-Host "  Installed $copiedSkills skills to $OpencodeDir\skills\"
Write-Host ""
Write-Host "Restart your Opencode session to use them."
