from app import create_app

rest = create_app()

if __name__ == '__main__':
    rest.run(
        host=rest.config['HOST'],
        port=rest.config['PORT'],
        debug=rest.config['DEBUG']
    )
