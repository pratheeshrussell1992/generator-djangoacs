'use strict';
const Generator = require('yeoman-generator');

//https://dzone.com/articles/create-your-own-yeoman
module.exports = class extends Generator {
  prompting() {
    // Have Yeoman greet the user.
    this.log(`Welcome to the Django Template generator for ACS!`);
    var prompts = [
      {
        type: "input",
        name: "project_name",
        message: "What is the name of your project?",
        default: this.appname
      },
      {type: 'list',
      name: 'databasetypes',
      message:'Choose your database type?',
      choices: [{
        name: 'SQLite',
        value: 'sqlite',
        checked: false
       },{
        name: 'MySQL',
        value: 'mysql',
        checked: true
       },{
        name: 'PostgreSQL',
        value: 'postgres',
        checked: false
       },{
        name: 'MongoDB',
        value: 'mongo',
        checked: false
       }]},
   {
      type: 'list',
      name: 'authtypes',
      message:'What kind of authentication do you want to use?',
      choices: [ {
       name: 'OAuth',
       value: 'oauth',
       checked: true},
       {
        name: 'JWT',
        value: 'jwt',
        checked: true}
  
  ]
   }
 ];

    return this.prompt(prompts).then(props => {
      // To access props later use this.props.someAnswer;
      this.props = props;
    });
  }

  writing() {
    this.fs.copyTpl(
      this.templatePath("common/!(apicore){**/*,*}"),
      this.destinationRoot(),this.props
    );
    this.fs.copyTpl(
      this.templatePath(`common/apicore/**/*`),
      this.destinationPath(`src/${this.props.project_name}`),this.props
    );
    // setup DB
    this.fs.copy(
      this.templatePath(`db/${this.props.databasetypes}/database.py`),
      this.destinationPath(`src/${this.props.project_name}/database.py`)
    );
     // add db requirements
    this.fs.copyTpl(
      this.templatePath(`db/${this.props.databasetypes}/requirements.txt`),
      this.destinationPath(`src/requirements.db.txt`)
    );

    //AUTH settings
    this.fs.copy(
      this.templatePath(`auth/${this.props.authtypes}/auth_setting.py`),
      this.destinationPath(`src/${this.props.project_name}/auth_setting.py`)
    );

    this.fs.copy(
      this.templatePath(`auth/${this.props.authtypes}/requirements.txt`),
      this.destinationPath(`src/requirements.auth.txt`)
    );

    this.fs.copy(
      this.templatePath(`auth/${this.props.authtypes}/${this.props.authtypes}LoginController.py`),
      this.destinationPath(`src/modules/user/controllers/${this.props.authtypes}LoginController.py`)
    );

    this.fs.copy(
      this.templatePath(`auth/${this.props.authtypes}/urls.py`),
      this.destinationPath(`src/modules/user/urls.py`)
    );

  }

};