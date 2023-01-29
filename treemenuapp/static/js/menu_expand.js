    $(function () {
      $('.tree li:has(ul)').addClass('parent_li').find(' > span')
      .attr('title', 'Collapse this branch');
       $('.tree li.parent_li > span').on('click', function (e) {
          var children = $(this).parent('li.parent_li').find(' > ul ');
          children.hide('fast');
          if (children.is(":visible")) {
              children.hide('fast');
              $(this).attr('title', 'Expand this branch').find(' > i')
              .addClass('fa-square-plus').removeClass('fa-square-minus');
          } else {
              children.show('fast');
              $(this).attr('title', 'Collapse this branch').find(' > i')
              .addClass('fa-square-minus').removeClass('fa-square-plus');
          }
          e.stopPropagation();
      });
      $('.tree > ul > li  ul:has(li)').hide();
      if ($('li.last')) {
        $.fn.find_root_from_current = function (elem) {
        debugger
        children = $(elem).find(' > ul');
        if ($(children).is('ul')) {
            children.show();
        }
        let parent = $(elem).parent()
        if ($(parent).is('ul')) {
            parent.show();
         }
         if ($(parent).is('.tree')) {
            return true;
         } else {
            $.fn.find_root_from_current(parent);
         }
      };
      $.fn.find_root_from_current('li.current');
      }
        debugger
      $('li.last').find('ul').hide();
//      if (elem) {
//        elem.forEach((item) => {
//            item.hide('fast');
//        })
//      }

  });

