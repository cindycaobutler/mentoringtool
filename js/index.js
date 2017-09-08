'use strict';

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var _React = React;
var Component = _React.Component;
var _ReactRedux = ReactRedux;
var Provider = _ReactRedux.Provider;
var _Redux = Redux;
var createStore = _Redux.createStore;
var applyMiddleware = _Redux.applyMiddleware;
var _ReactReduxForm = ReactReduxForm;
var Field = _ReactReduxForm.Field;
var Control = _ReactReduxForm.Control;
var Form = _ReactReduxForm.Form;
var combineForms = _ReactReduxForm.combineForms;

var thunk = ReduxThunk.default;
var logger = reduxLogger();

var initialUserState = {
  firstName: '',
  lastName: '',
  city: "",
  state: "",
  age_range: "",
  // contact: "",
  email: "",
  phone: "",
  // education: "",
  major: "",
  degree: "",
  // workExperience: "",
  jobCategory: "",
  level: "",
  mentor: "mentor",
  interests: "",
  password: ''

};

var store = createStore(combineForms({
  user: initialUserState
}), applyMiddleware(thunk));

var UserForm = function (_Component) {
  _inherits(UserForm, _Component);

  function UserForm() {
    _classCallCheck(this, UserForm);

    return _possibleConstructorReturn(this, _Component.apply(this, arguments));
  }

  UserForm.prototype.render = function render() {
    return React.createElement(
      Form,
      { model: 'user', onSubmit: function onSubmit(v) {
          return console.log(v);
        } },
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'First name:'
        ),
        React.createElement(Control.text, { model: '.firstName', placeholder: 'First Name' })
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'Last name:'
        ),
        React.createElement(Control.text, { model: '.lastName', placeholder: 'Last Name' })
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'City:'
        ),
        React.createElement(Control, { model: '.city', type: 'city', placeholder: '' })
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'State:'
        ),
        React.createElement(Control, { model: '.city', type: 'city', placeholder: '' })
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'Age Range:'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: 'under20' }),
          ' Under 20'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '20to25' }),
          ' 20-25'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '26to30' }),
          ' 26-30'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '31to35' }),
          ' 31-35'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '36to40' }),
          ' 36-40'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '41to45' }),
          ' 41-45'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '46to50' }),
          ' 46-50'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '51to55' }),
          ' 51-55'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.radio, { model: '.age', value: '56plus' }),
          ' 56+'
        )
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'Email:'
        ),
        React.createElement(Control, { model: '.email', type: 'email', placeholder: 'something@example.com' })
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'Phone:'
        ),
        React.createElement(Control, { model: '.phone', type: 'phone', placeholder: '(111) 111-1111' })
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'Major'
        ),
        React.createElement(
          Control.select,
          { model: '.major' },
          React.createElement('option', { value: '' }),
          React.createElement(
            'option',
            { value: 'associate\'s' },
            'Associate'
          ),
          React.createElement(
            'option',
            { value: 'bachelor\'s' },
            'Bachelor'
          ),
          React.createElement(
            'option',
            { value: 'master\'s' },
            'Master'
          ),
          React.createElement(
            'option',
            { value: 'doctoral' },
            'Ph.D.'
          ),
          React.createElement(
            'option',
            { value: 'professional' },
            'Professional'
          ),
          React.createElement(
            'option',
            { value: 'other' },
            'Other'
          )
        )
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'Degree'
        ),
        React.createElement(
          Control.select,
          { model: '.major' },
          React.createElement('option', { value: '' }),
          React.createElement(
            'option',
            { value: '' },
            'Accounting'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Agriculture'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Anthropology'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Architecture'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Art'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Artifical Intelligence'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Aviation'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Biology'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Biochemistry'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Biomedical Engineering'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Business Administration'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Chemical Engieering'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Civil Engineering'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Communications'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Computer and Information Science'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Computer Engineering'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Computer Graphics'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Computer Science'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Computer Systems Analysis'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Economics'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Education'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Electrical Engineering'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Engieering'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Entrepreneurship'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Ethnic Studies'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Fiance'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Government'
          ),
          React.createElement(
            'option',
            { value: '' },
            'History'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Human Resources'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Information Technology'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Marketing'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Mathematics'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Other'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Pharmacy'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Political Science'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Pyschology'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Real Estate'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Sociology'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Statistics'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Technical Writing'
          ),
          React.createElement(
            'option',
            { value: '' },
            'Web Design'
          )
        )
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'School:'
        ),
        React.createElement(Control, { model: '.school', type: 'school', placeholder: '' })
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'You do wish to be a mentor or mentee?'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.checkbox, { model: '.mentor', value: 'mentor' }),
          ' mentor'
        ),
        React.createElement(
          'label',
          null,
          React.createElement(Control.checkbox, { model: '.mentee', value: 'mentee' }),
          ' mentee'
        )
      ),
      React.createElement(
        'div',
        { className: 'field' },
        React.createElement(
          'label',
          null,
          'Interests'
        ),
        React.createElement(Control.textarea, { model: '.notes' })
      ),
      React.createElement(
        'button',
        { type: 'submit' },
        'Submit'
      ),
      React.createElement(
        Control.reset,
        { model: 'user', className: 'secondary' },
        'Clear Values'
      )
    );
  };

  return UserForm;
}(Component);

var App = function (_React$Component) {
  _inherits(App, _React$Component);

  function App() {
    _classCallCheck(this, App);

    return _possibleConstructorReturn(this, _React$Component.apply(this, arguments));
  }

  App.prototype.render = function render() {
    return React.createElement(
      Provider,
      { store: store },
      React.createElement(UserForm, null)
    );
  };

  return App;
}(React.Component);

ReactDOM.render(React.createElement(App, null), document.getElementById('app'));