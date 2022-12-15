pipeline{
  agent any
  stages{
    stage('version'){
      steps{
        sh 'python3 --version'
      }
    }
    stage('Collect'){
      steps{
        sh 'python3 Get_Spent_Amount.py'
      }
    }
  }
}
