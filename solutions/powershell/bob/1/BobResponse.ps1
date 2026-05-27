Function Get-BobResponse() {
    <#
    .SYNOPSIS
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.
    
    .DESCRIPTION
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question.

    He answers 'Whoa, chill out!' if you yell at him.

    He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

    He says 'Fine. Be that way!' if you address him without actually saying
    anything.

    He answers 'Whatever.' to anything else.
    
    .PARAMETER HeyBob
    The sentence you say to Bob.
    
    .EXAMPLE
    Get-BobResponse -HeyBob "Hi Bob"
    #>
    [CmdletBinding()]
    Param(
        [string]$HeyBob
    )

    $trim = $HeyBob.Trim()

    $isSilence = [string]::IsNullOrWhiteSpace($HeyBob)

    $isQuestion = $trim.EndsWith('?')

    $hasUpper = $HeyBob -cmatch '[A-Z]'
    $hasLower = $HeyBob -cmatch '[a-z]'
    $isYell = $hasUpper -and (-not $hasLower)
    
    if ($isSilence) {return 'Fine. Be that way!'}
    elseif ($isYell -and $isQuestion) {return "Calm down, I know what I'm doing!"}
    elseif ($isYell) {return "Whoa, chill out!"}
    elseif ($isQuestion) {return "Sure."}
    else {return "Whatever."}
}
