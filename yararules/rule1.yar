rule Rule1
{
    strings:
        $text_string = "trojan_virus"

    condition:
       $text_string
}