<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [The Secret of Love :](#the-secret-of-love-)
      - [Everyone wants to hide their secrets, especially if those are their love's secrets](#everyone-wants-to-hide-their-secrets-especially-if-those-are-their-loves-secrets)
    - [The cipher algorithm is :](#the-cipher-algorithm-is-)
    - [Input](#input)
    - [Output](#output)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# The Secret of Love :
#### Everyone wants to hide their secrets, especially if those are their love's secrets
:bulb: **To help them we will write a cipher for their secrets.**

There will be inputs : :secret: the secret  , :gift_heart: love name,  :birthday: year of birth.

> **Secret condition** :point_up: : The secret must be at least **8** **characters**.

### The cipher algorithm is :
* Concatenate the love secret with the love name     :arrow_heading_down:
* Reverse the string :arrow_heading_down:
* Concatenate the revered string with the  year of birth :arrow_heading_down:

>  ***NOTE:*** We need to cipher the secret itself , not to create a new  ciphered string.

### Input
```
*secret:* this_is_my_secret  
*name:* Max  
*year:* 1982  
```

### Output
```
xaMterces_ym_si_siht1982
```