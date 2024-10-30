pipeline {
    agent any

    environment{
        PYTHON_VERSION = '3.12'
        VENV_DIR = 'venv'
    }

    stages {
    stage('Installing Python') {
            steps {
                script {
                    sh """
                        if [ -d "\$HOME/.pyenv" ]; then
                            echo "Python is already exists."
                        else
                            echo "Installing pyenv..."
                            curl https://pyenv.run | bash

                            export PATH="\$HOME/.pyenv/bin:\$PATH"
                            eval "\$(pyenv init --path)"
                            eval "\$(pyenv init -)"

                            pyenv install ${PYTHON_VERSION}
                            pyenv global ${PYTHON_VERSION}
                        fi

                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"
                    """
                }
            }
        }

        stage("Creation of Python virtual environment") {
            steps{
                script {
                    sh """
                        source ~/.bashrc

                        if [ ! -d "\$(VENV_DIR) "]; then
                            echo "Creating virtual environment"
                            python3 -m venv \$(VENV_DIR)
                        else
                            echo "Virtual environment already exists."
                        fi
                    """
                }
            }
        }

        stage("Activation of venv and installing dependencies then execute test cases.") {
            steps{
                script {
                    sh """
                        source ~/.bashrc
                        source ${VENV_DIR}/bin/activate

                        pip install --upgrade pip
                        pip install -r requirements.txt

                        pytest --maxfail=1 --disable-warnings -q lesson_30/test_package_getting.py
                    """
                }
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/VeronikaDi/aqa_VDimova_l2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '/opt/homebrew/bin/python3.10 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '/opt/homebrew/bin/python3.10 -m pytest lesson_30/test_package_getting.py --junitxml=test-results.xml'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }

    post {
        always {
            emailext(
                to: 'InsertYour@Mail.Here',
                subject: "Testing results Jenkins Pipeline",
                body: "Pipeline finished. Check results of the tests on page Build."
            )
        }
    }
}
