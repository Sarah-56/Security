rule Rule0
{
    strings:
        $text_string = "virusvirus"

    condition:
       $text_string
}