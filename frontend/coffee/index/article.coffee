$ ->
  $('body').on 'click', '.btn-idontknow', (e)->
    e.preventDefault()

    alert '我还没想好这个按钮用来干什么...'
