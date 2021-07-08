function openNav() {
  document.querySelector('.landing-nav')?.classList?.add('open')
}
function closeNav() {
  document.querySelector('.landing-nav')?.classList?.remove('open')
}
function signupLoginBtnOpen() {
  document.querySelector('.landing-nav')?.classList?.add('open-auth');
}
function signupLoginBtnClose() {
  document.querySelector('.landing-nav')?.classList?.remove('open-auth');
}