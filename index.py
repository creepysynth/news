#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from genshi.template import TemplateLoader
from router import Router, NotFoundError

def home(environ, tmpl):
    stream = tmpl.generate(
        home={'class':'active'},
        politics={'class':None},
        business={'class':None},
        sports={'class':None},
        science={'class':None},
        entertainment={'class':None},
        health={'class':None},
        title='WorldWideNews',
        main_href='/news/science/space',
        main_img='/static/science/space/161107162522-nasa-1-exlarge-169.jpg',
        main_alt='space',
        main_header='Going to space is a real pain in the back',
        main_text='''Six-month stay on the International Space Station can be a pain 
            in the back for astronauts. While they may gain up to 2 inches in height 
            temporarily, that effect is accompanied by a weakening of the muscles 
            supporting the spine, according to a new study. Astronauts have been 
            reporting back pain since the late 1980s, when space missions grew longer.''',
        side1_href='/news/science/space',
        side1_img='/static/home/side1.jpg',
        side1_alt='mccain',
        side1_desc="Russian election-related hacks threaten to 'destroy democracy'",
        side2_href='/news/science/space',
        side2_img='/static/home/side2.jpg',
        side2_alt='refugee girl',
        side2_desc="Out of Mosul, into limbo: The refugees fleeing ISIS",
        col1_href='/news/science/space',
        col1_img='/static/home/col1.jpg',
        col1_alt='theatre',
        col1_desc="High-tech Hollywood makeover for Shakespeare",
        col2_href='/news/science/space',
        col2_img='/static/home/col2.jpg',
        col2_alt='putin and obama',
        col2_desc="Obama: 'A brazen Russia must face US retribution'",
        col3_href='/news/science/space',
        col3_img='/static/home/col3.jpg',
        col3_alt='a runner',
        col3_desc="Weird and unexpected things that happen when you run",
        col4_href='/news/science/space',
        col4_img='/static/home/col4.jpg',
        col4_alt='skyscraper',
        col4_desc="MahaNakhon: Why Asia's futuristic skylines just got crazier",
        col5_href='/news/science/space',
        col5_img='/static/home/col5.jpg',
        col5_alt='donald trump',
        col5_desc="Donald Trump: Man of the year, or sitting duck president?",
        col6_href='/news/science/space',
        col6_img='/static/home/col6.jpg',
        col6_alt='slums',
        col6_desc="Malaysia: Myanmar's crisis a threat to regional stability",
    )
    html = stream.render('html', doctype='html5')
    return (('200 OK', [('Content-Type','text/html')]),
            [html.encode('utf-8')])

def category(environ, tmpl):
    categories = (
        'politics',
        'business',
        'sports',
        'science',
        'entertainment',
        'health'
    )
    relative = environ['PATH_INFO'][6:]
    navigation = {}

    for category in categories:
        if category == relative:
            navigation[category] = {'class':'active'}
        else:
            navigation[category] = {'class':None}
    stream = tmpl.generate(
        home={'class':None},
        title=relative.title(),
        main_href='/news/science/space',
        main_img='http://lorempixel.com/960/540/abstract',
        main_alt='lorem ipsum',
        main_header='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        main_text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Nulla quam velit, vulputate eu pharetra nec, mattis ac neque. Duis 
            vulputate commodo lectus, ac blandit elit tincidunt id. Sed rhoncus, 
            tortor sed eleifend tristique, tortor mauris molestie elit, et 
            lacinia ipsum quam nec dui. Quisque nec mauris sit amet elit iaculis 
            pretium sit amet quis magna.''',
        side1_href='/news/science/space',
        side1_img='http://lorempixel.com/480/270/abstract',
        side1_alt='lorem ipsum',
        side1_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        side2_href='/news/science/space',
        side2_img='http://lorempixel.com/480/270/abstract',
        side2_alt='lorem ipsum',
        side2_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        col1_href='/news/science/space',
        col1_img='http://lorempixel.com/480/270/abstract',
        col1_alt='lorem ipsum',
        col1_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        col2_href='/news/science/space',
        col2_img='http://lorempixel.com/480/270/abstract',
        col2_alt='lorem ipsum',
        col2_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        col3_href='/news/science/space',
        col3_img='http://lorempixel.com/480/270/abstract',
        col3_alt='lorem ipsum',
        col3_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        col4_href='/news/science/space',
        col4_img='http://lorempixel.com/480/270/abstract',
        col4_alt='lorem ipsum',
        col4_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        col5_href='/news/science/space',
        col5_img='http://lorempixel.com/480/270/abstract',
        col5_alt='lorem ipsum',
        col5_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        col6_href='/news/science/space',
        col6_img='http://lorempixel.com/480/270/abstract',
        col6_alt='lorem ipsum',
        col6_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        **navigation
    )
    html = stream.render('html', doctype='html5')
    return (('200 OK', [('Content-Type','text/html')]),
            [html.encode('utf-8')])

def article(environ, tmpl):
    block_main = [
    '''Six-month stay on the International Space Station can be a pain in the back
        for astronauts. While they may gain up to 2 inches in height temporarily, that
        effect is accompanied by a weakening of the muscles supporting the spine, 
        according to a new study.''',
    '''Astronauts have been reporting back pain since the late 1980s, when space
        missions grew longer. Their flight medical data show that more than half
        of US astronauts have reported back pain, especially in their lower backs.
        Up to 28% indicated that it was moderate to severe pain, sometimes lasting
        the duration of their mission.''',
    '''Things don't improve when they return to Earth's gravity. In the first year
        after their mission, astronauts have a 4.3 times higher risk of a herniated
        disc.''',
    '''"It's sort of an ongoing problem that has been a significant one with cause
        for concern," said Dr. Douglas Chang, first author of the new study and
        associate professor of orthopedic surgery and chief of physical medicine
        and rehabilitation service at University of California San Diego Health.
        "So this study is the first to take it from just an epidemiological
        description and look at the possible mechanisms for what is going on
        with the astronauts' backs."'''
    ]
    block_1 = [
    '''Much attention has been focused on intervertebral discs, the spongy shock
        absorbers that sit between our vertebrae, as the culprit for the back issues
        that astronauts face. But the new study runs counter to that thinking. In this
        research, funded by NASA, Chang's team observed little to no changes in the
        discs, their height or swelling''',
    '''What they did observe in six astronauts who spent four to seven months on the
        ISS was a tremendous degeneration and atrophying of the supporting musculature
        in the lumbar (lower) spine, Chang said. These muscles are the ones that help
        us stay upright, walk and move our upper extremities in an environment like
        Earth, while protecting discs and ligaments from strain or injury.''',
    '''In microgravity, the torso lengthens, most likely due to spinal unloading, in
        which the spinal curvature flattens. Astronauts also aren't using the muscle
        tone in their lower backs because they aren't bending over or using their lower
        backs to move, like on Earth, Chang said. This is where the pain and stiffening
        occurs, much like if the astronauts were in a body cast for six months.''',
    '''MRI scans before and after the missions revealed that the astronauts experienced
        a 19% decrease in these muscles during their flight. "Even after six weeks of
        training and reconditioning here one Earth, they are only getting about 68% of
        their losses restored," Chang explained.''',
    '''Chang and his team consider this a serious issue for long-term manned missions,
        especially when considering a trip to Mars that could take eight or nine months
        just to reach the Red Planet. That trip, and the astronauts' potential time
        spent in Martian gravity 38% of the surface gravity on Earth creates the
        potential for muscle atrophy and deconditioning.''',
    '''The team's future research will also look at reported neck issues, where there
        can be even more occurrences of muscle atrophy and a slower recovery period.
        They are also hoping to partner with another university on inflight ultrasounds
        of the spine, to look at what happens to astronauts while they are on the space
        station.'''
    ]
    block_2 = [
    '''Because nobody likes back pain and muscle loss, Chang suggested countermeasures
        that should be added to the already two- to three-hour workout astronauts have
        on the space station each day. Though their exercise machines focus on a range
        of issues including cardiovascular and skeletal health, the team believes that
        space travelers also need to include a core-strenghtening program focused on
        the spine.''',
    '''In addition to the "fetal tuck" position astronauts use in microgravity to
        stretch their lower back or alleviate back pain, Chang suggested yoga. But
        he knows that is easier said than done.''',
    '''"A lot of yoga depends on the effects of gravity, like downward dog, where a
        stretch through the hamstring, calf muscles, back of the neck and shoulders
        are possible because of gravity. When you remove that, you may not have the
        same benefit."''',
    '''Any machines on the space station also have to be designed with regards to
        weight, size and even the reverberations they could produce on the station.''',
    '''Chang and the other researchers brainstormed with a virtual reality team
        about different exercise programs that would enable astronauts to invite
        friends, family or even Twitter followers to join them in a virtual workout,
        making the daily repetition of their workouts more fun and competitive.''',
    '''One of Chang's teammates has felt this pain personally. Dr. Scott Parazynski
        is the only astronaut to summit Mount Everest. He experienced a herniated
        disc after returning from the ISS to Earth. Less than a year later, when he
        attempted to climb Everest the first time, he had to be airlifted off. After
        a rehabilitation process, he eventually made the summit. Now, he speaks to
        current astronauts about the ways they can contribute to studies about their
        health in microgravity.''',
    '''Keeping the astronauts healthy and fit is the least they can do, Chang said.''',
    '''"When a crew comes back, they say on one side of the space station, they see
        this beautiful blue planet," he said. "Everything they hold dear to them is
        on this fragile little planet. And they look out the other window and just
        see infinity stretching off into the blackness, and they come back with a
        different sense of themselves and their place in the universe.''',
    '''"All of them are committed to furthering space knowledge and making
        incremental steps forward in any way they can for the next crew."'''
    ]
    stream = tmpl.generate(
        home={'class':None},
        politics={'class':None},
        business={'class':None},
        sports={'class':None},
        science={'class':'active'},
        entertainment={'class':None},
        health={'class':None},
        author='By Ashley Strickland',
        header_main='Going to space is a real pain in the back',
        main_img='/static/science/space/161107162522-nasa-1-exlarge-169.jpg',
        main_img_alt='space',
        block_main=block_main,
        block_1_header='Like being in a body cast',
        block_1=block_1,
        block_1_img='/static/science/space/161025161047-03-spine-health-space-exlarge-169.jpg',
        block_1_img_alt='astronaut in open space',
        block_2_header='Yoga in space?',
        block_2=block_2,
        block_2_img='',
        block_2_img_alt='',
        block_3_header='',
        block_3=[],
        block_3_img='',
        block_3_img_alt='',
        published='Published 21.49 GMT (05.49 HKT) November 7, 2016'
    )
    html = stream.render('html', doctype='html5')
    return (('200 OK', [('Content-Type','text/html')]),
            [html.encode('utf-8')])

def not_found(*args):
    return (('404 Not Found', [('Content-Type','text/html')]),
            ['<h1 style="text-align:center">404 Not Found</h1>'.encode('utf-8')])

def application(environ, start_response):
    path = environ['PATH_INFO']
    routes = open('configs/routes.conf').read().split('\n')
    try:
        route = Router(routes).route_for_uri(path)
    except NotFoundError:
        response, data = not_found()
    else:
        handler = {
            '/':                    home,
            '/news':                home,
            '/news/politics':       category,
            '/news/business':       category,
            '/news/sports':         category,
            '/news/science':        category,
            '/news/entertainment':  category,
            '/news/health':         category,
            '/news/science/space':  article
        }
        tmpl = TemplateLoader('').load(route)    
        response, data = handler.get(path, not_found)(environ, tmpl)        
    start_response(*response)
    return data
