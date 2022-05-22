# Simple YAML to XML
Script converter of YAML to XML. Written in Python 3

## Example
```
day_body:
  subject:
    - day: Ср
      time:
        - time: 10:00-11:30
          week: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
      room:
        - room: 369A АУД.
          location: ул.Ломоносова, д.49, лит. А
      lesson: Дискретная Математика(Прак)
      teacher: Поляков Владимир Иванович
      format: Очно - дистанционный
```
Result in
```
<?xml version="1.0" encoding="UTF-8"?>
<day_body>
  <subject>
    <day>Ср</day>
    <time>
      <time>10:00-11:30</time>
      <week>2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17</week>
    </time>
    <room>
      <room>369A АУД.</room>
      <location>ул.Ломоносова, д.49, лит. А</location>
    </room>
    <lesson>Дискретная Математика(Прак)</lesson>
    <teacher>Поляков Владимир Иванович</teacher>
    <format>Очно - дистанционный</format>
     </subject>
</day_body>
```
## Information
* This is a simple script that parses an YAML file to XML
* This is testing and sampling purposes but can be changed to production ready
* This should be run in an isolated python environment (virtual env)

## Requirements
* Python 3.6+
