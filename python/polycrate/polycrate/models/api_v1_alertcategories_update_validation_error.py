from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertcategories_update_active_error_component import (
        ApiV1AlertcategoriesUpdateActiveErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_annotations_error_component import (
        ApiV1AlertcategoriesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_archived_at_error_component import (
        ApiV1AlertcategoriesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_archived_error_component import (
        ApiV1AlertcategoriesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_archived_reason_error_component import (
        ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_criticality_error_component import (
        ApiV1AlertcategoriesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_debug_mode_error_component import (
        ApiV1AlertcategoriesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_description_error_component import (
        ApiV1AlertcategoriesUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_display_name_error_component import (
        ApiV1AlertcategoriesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_kind_error_component import ApiV1AlertcategoriesUpdateKindErrorComponent
    from ..models.api_v1_alertcategories_update_labels_error_component import (
        ApiV1AlertcategoriesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_name_error_component import ApiV1AlertcategoriesUpdateNameErrorComponent
    from ..models.api_v1_alertcategories_update_non_field_errors_error_component import (
        ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_platform_service_error_component import (
        ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_provider_error_component import (
        ApiV1AlertcategoriesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_provider_id_error_component import (
        ApiV1AlertcategoriesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_provider_reference_error_component import (
        ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_reconciliation_enabled_error_component import (
        ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_sla_availability_error_component import (
        ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_sla_target_error_component import (
        ApiV1AlertcategoriesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_slo_availability_error_component import (
        ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_slo_target_error_component import (
        ApiV1AlertcategoriesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_sort_order_error_component import (
        ApiV1AlertcategoriesUpdateSortOrderErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_target_availability_error_component import (
        ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_update_tolerations_error_component import (
        ApiV1AlertcategoriesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertcategoriesUpdateValidationError")


@_attrs_define
class ApiV1AlertcategoriesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertcategoriesUpdateActiveErrorComponent |
            ApiV1AlertcategoriesUpdateAnnotationsErrorComponent | ApiV1AlertcategoriesUpdateArchivedAtErrorComponent |
            ApiV1AlertcategoriesUpdateArchivedErrorComponent | ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent |
            ApiV1AlertcategoriesUpdateCriticalityErrorComponent | ApiV1AlertcategoriesUpdateDebugModeErrorComponent |
            ApiV1AlertcategoriesUpdateDescriptionErrorComponent | ApiV1AlertcategoriesUpdateDisplayNameErrorComponent |
            ApiV1AlertcategoriesUpdateKindErrorComponent | ApiV1AlertcategoriesUpdateLabelsErrorComponent |
            ApiV1AlertcategoriesUpdateNameErrorComponent | ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent |
            ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent | ApiV1AlertcategoriesUpdateProviderErrorComponent |
            ApiV1AlertcategoriesUpdateProviderIdErrorComponent | ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent |
            ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent |
            ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent | ApiV1AlertcategoriesUpdateSlaTargetErrorComponent |
            ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent | ApiV1AlertcategoriesUpdateSloTargetErrorComponent |
            ApiV1AlertcategoriesUpdateSortOrderErrorComponent | ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent |
            ApiV1AlertcategoriesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertcategoriesUpdateActiveErrorComponent
        | ApiV1AlertcategoriesUpdateAnnotationsErrorComponent
        | ApiV1AlertcategoriesUpdateArchivedAtErrorComponent
        | ApiV1AlertcategoriesUpdateArchivedErrorComponent
        | ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent
        | ApiV1AlertcategoriesUpdateCriticalityErrorComponent
        | ApiV1AlertcategoriesUpdateDebugModeErrorComponent
        | ApiV1AlertcategoriesUpdateDescriptionErrorComponent
        | ApiV1AlertcategoriesUpdateDisplayNameErrorComponent
        | ApiV1AlertcategoriesUpdateKindErrorComponent
        | ApiV1AlertcategoriesUpdateLabelsErrorComponent
        | ApiV1AlertcategoriesUpdateNameErrorComponent
        | ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent
        | ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent
        | ApiV1AlertcategoriesUpdateProviderErrorComponent
        | ApiV1AlertcategoriesUpdateProviderIdErrorComponent
        | ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent
        | ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent
        | ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent
        | ApiV1AlertcategoriesUpdateSlaTargetErrorComponent
        | ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent
        | ApiV1AlertcategoriesUpdateSloTargetErrorComponent
        | ApiV1AlertcategoriesUpdateSortOrderErrorComponent
        | ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent
        | ApiV1AlertcategoriesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertcategories_update_annotations_error_component import (
            ApiV1AlertcategoriesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_archived_at_error_component import (
            ApiV1AlertcategoriesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_archived_error_component import (
            ApiV1AlertcategoriesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_archived_reason_error_component import (
            ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_criticality_error_component import (
            ApiV1AlertcategoriesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_debug_mode_error_component import (
            ApiV1AlertcategoriesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_description_error_component import (
            ApiV1AlertcategoriesUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_display_name_error_component import (
            ApiV1AlertcategoriesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_kind_error_component import (
            ApiV1AlertcategoriesUpdateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_labels_error_component import (
            ApiV1AlertcategoriesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_name_error_component import (
            ApiV1AlertcategoriesUpdateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_non_field_errors_error_component import (
            ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_platform_service_error_component import (
            ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_provider_error_component import (
            ApiV1AlertcategoriesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_provider_id_error_component import (
            ApiV1AlertcategoriesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_provider_reference_error_component import (
            ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_sla_availability_error_component import (
            ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_sla_target_error_component import (
            ApiV1AlertcategoriesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_slo_availability_error_component import (
            ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_slo_target_error_component import (
            ApiV1AlertcategoriesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_sort_order_error_component import (
            ApiV1AlertcategoriesUpdateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_target_availability_error_component import (
            ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_tolerations_error_component import (
            ApiV1AlertcategoriesUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesUpdateSortOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_alertcategories_update_active_error_component import (
            ApiV1AlertcategoriesUpdateActiveErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_annotations_error_component import (
            ApiV1AlertcategoriesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_archived_at_error_component import (
            ApiV1AlertcategoriesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_archived_error_component import (
            ApiV1AlertcategoriesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_archived_reason_error_component import (
            ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_criticality_error_component import (
            ApiV1AlertcategoriesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_debug_mode_error_component import (
            ApiV1AlertcategoriesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_description_error_component import (
            ApiV1AlertcategoriesUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_display_name_error_component import (
            ApiV1AlertcategoriesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_kind_error_component import (
            ApiV1AlertcategoriesUpdateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_labels_error_component import (
            ApiV1AlertcategoriesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_name_error_component import (
            ApiV1AlertcategoriesUpdateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_non_field_errors_error_component import (
            ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_platform_service_error_component import (
            ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_provider_error_component import (
            ApiV1AlertcategoriesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_provider_id_error_component import (
            ApiV1AlertcategoriesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_provider_reference_error_component import (
            ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_sla_availability_error_component import (
            ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_sla_target_error_component import (
            ApiV1AlertcategoriesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_slo_availability_error_component import (
            ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_slo_target_error_component import (
            ApiV1AlertcategoriesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_sort_order_error_component import (
            ApiV1AlertcategoriesUpdateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_target_availability_error_component import (
            ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_update_tolerations_error_component import (
            ApiV1AlertcategoriesUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertcategoriesUpdateActiveErrorComponent
                | ApiV1AlertcategoriesUpdateAnnotationsErrorComponent
                | ApiV1AlertcategoriesUpdateArchivedAtErrorComponent
                | ApiV1AlertcategoriesUpdateArchivedErrorComponent
                | ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent
                | ApiV1AlertcategoriesUpdateCriticalityErrorComponent
                | ApiV1AlertcategoriesUpdateDebugModeErrorComponent
                | ApiV1AlertcategoriesUpdateDescriptionErrorComponent
                | ApiV1AlertcategoriesUpdateDisplayNameErrorComponent
                | ApiV1AlertcategoriesUpdateKindErrorComponent
                | ApiV1AlertcategoriesUpdateLabelsErrorComponent
                | ApiV1AlertcategoriesUpdateNameErrorComponent
                | ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent
                | ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent
                | ApiV1AlertcategoriesUpdateProviderErrorComponent
                | ApiV1AlertcategoriesUpdateProviderIdErrorComponent
                | ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent
                | ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent
                | ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent
                | ApiV1AlertcategoriesUpdateSlaTargetErrorComponent
                | ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent
                | ApiV1AlertcategoriesUpdateSloTargetErrorComponent
                | ApiV1AlertcategoriesUpdateSortOrderErrorComponent
                | ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent
                | ApiV1AlertcategoriesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_0 = (
                        ApiV1AlertcategoriesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_1 = (
                        ApiV1AlertcategoriesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_2 = (
                        ApiV1AlertcategoriesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_3 = (
                        ApiV1AlertcategoriesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_4 = (
                        ApiV1AlertcategoriesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_5 = (
                        ApiV1AlertcategoriesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_6 = (
                        ApiV1AlertcategoriesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_7 = (
                        ApiV1AlertcategoriesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_8 = (
                        ApiV1AlertcategoriesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_9 = (
                        ApiV1AlertcategoriesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_10 = (
                        ApiV1AlertcategoriesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_11 = (
                        ApiV1AlertcategoriesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_12 = (
                        ApiV1AlertcategoriesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_13 = (
                        ApiV1AlertcategoriesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_14 = (
                        ApiV1AlertcategoriesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_15 = (
                        ApiV1AlertcategoriesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_16 = (
                        ApiV1AlertcategoriesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_17 = (
                        ApiV1AlertcategoriesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_18 = (
                        ApiV1AlertcategoriesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_19 = (
                        ApiV1AlertcategoriesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_20 = (
                        ApiV1AlertcategoriesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_21 = (
                        ApiV1AlertcategoriesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_22 = (
                        ApiV1AlertcategoriesUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_update_error_type_23 = (
                        ApiV1AlertcategoriesUpdateSortOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertcategories_update_error_type_24 = (
                    ApiV1AlertcategoriesUpdateActiveErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertcategories_update_error_type_24

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertcategories_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertcategories_update_validation_error.additional_properties = d
        return api_v1_alertcategories_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
