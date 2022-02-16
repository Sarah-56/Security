rule Rule2
{
    strings:
        $text_string = "virus"

    condition:
       $text_string
}
