document.querySelector('.read-more').addEventListener('click', function() {
    var moreContent = document.querySelector('.more-content');
    if (moreContent.style.display === 'none' || moreContent.style.display === '') {
        moreContent.style.display = 'block';
        this.innerHTML = '... Read less'; // Change button text to "Read less"
    } else {
        moreContent.style.display = 'none';
        this.innerHTML = '... Read more'; // Change button text back to "Read more"
    }
});
