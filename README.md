# Game of Thrones quotes client written in Python

A simple client to retrieve some quotes of the famous TV Show, Game of Thrones written in Python!

:globe_with_meridians: API Website: https://gameofthronesquotes.xyz/

All methods returns Python objects.

### Random quote

Get a random quote:

```Python
client = GameOfThronesClient()
client.random_quote()
```

### Random quote list

```Python
client.random_quote_list()
```

In this method you can change the quantity, by default it's `5`.

```Python
client.random_quote_list(quantity=10)
```

### Quote from character slug

```Python
client.quote_from_character_slug('jon')
```

### Quote list from character slug

```Python
client.quote_list_from_character_slug('jon')
```

In this method you can change the quantity, by default it's `5`.

```Python
client.quote_list_from_character_slug('jon', quantity=10)
```

### Houses

```Python
client.houses()
```

### House by slug

```Python
client.house_by_slug('stark')
```

### Characters

```Python
client.characters()
```

### Character by slug

```Python
client.character_by_slug('jon')
```

# Objects

## Member

`name`: `str`

`slug`: `str`

## House

`name`: `Optional[str] = None `

`slug`: `Optional[str] = None `

`members`: `Optional[List[Member]] = []`

## Character

`name`: `str`

`slug`: `str`

`house`: `Optional[House] = None`

`quotes`: `Optional[List[str]] = []`

## Quote

`sentence`: `str`

`character`: `Character`
