'use strict';
const Generator = require('yeoman-generator');
const fse = require('fs-extra');

//https://dzone.com/articles/create-your-own-yeoman
module.exports = class extends Generator {
  prompting() {
    // Have Yeoman greet the user.
    this.log(`Welcome to the Django Template generator for ACS!`);

    var prompts = [{
      type: 'list',
      name: 'databasetypes',
      message:'Choose your database type?',
      choices: [{
        name: 'SQLite',
        value: 'sqlite',
        checked: true
       }]
     },
   {
      type: 'list',
      name: 'authtypes',
      message:'What kind of authentication do you want to use?',
      choices: [ {
       name: 'OAuth',
       value: 'oauth',
       checked: true
   }]
   }
 ];

    return this.prompt(prompts).then(props => {
      // To access props later use this.props.someAnswer;
      this.props = props;
    });
  }

  writing() {
    this.log( "you chose" + this.props.authtypes);
    this.fs.copy(
      this.templatePath('basic/**/*'),
      this.destinationRoot()
    );
  }

};
