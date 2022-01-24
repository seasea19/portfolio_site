const left = document.querySelector('.left')
const right = document.querySelector('.right')
const container = document.querySelector('.container')

left .addEventListener('mouseenter', () => container.classtist.add('hover-left'))
left.addEventlistener('mouseleave', () => container.classlist.remove('hover-left'))

right. addEventListener('mouseenter', () => container.classtist.add('haver-right'))
right .addEventListener ('mouseleave', () => container.classtist.remove('hover-right'))