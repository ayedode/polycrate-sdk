from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conditions_update_annotations_error_component import (
        ApiV1ConditionsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_conditions_update_archived_at_error_component import (
        ApiV1ConditionsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_conditions_update_archived_error_component import ApiV1ConditionsUpdateArchivedErrorComponent
    from ..models.api_v1_conditions_update_archived_reason_error_component import (
        ApiV1ConditionsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_conditions_update_criticality_error_component import (
        ApiV1ConditionsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_conditions_update_debug_mode_error_component import (
        ApiV1ConditionsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_conditions_update_description_error_component import (
        ApiV1ConditionsUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_conditions_update_display_name_error_component import (
        ApiV1ConditionsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_conditions_update_is_system_error_component import ApiV1ConditionsUpdateIsSystemErrorComponent
    from ..models.api_v1_conditions_update_kind_error_component import ApiV1ConditionsUpdateKindErrorComponent
    from ..models.api_v1_conditions_update_labels_error_component import ApiV1ConditionsUpdateLabelsErrorComponent
    from ..models.api_v1_conditions_update_name_error_component import ApiV1ConditionsUpdateNameErrorComponent
    from ..models.api_v1_conditions_update_non_field_errors_error_component import (
        ApiV1ConditionsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_conditions_update_platform_service_error_component import (
        ApiV1ConditionsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_conditions_update_provider_error_component import ApiV1ConditionsUpdateProviderErrorComponent
    from ..models.api_v1_conditions_update_provider_id_error_component import (
        ApiV1ConditionsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_conditions_update_provider_reference_error_component import (
        ApiV1ConditionsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_conditions_update_reconciliation_enabled_error_component import (
        ApiV1ConditionsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_conditions_update_severity_error_component import ApiV1ConditionsUpdateSeverityErrorComponent
    from ..models.api_v1_conditions_update_sla_availability_error_component import (
        ApiV1ConditionsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_update_sla_target_error_component import (
        ApiV1ConditionsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_conditions_update_slo_availability_error_component import (
        ApiV1ConditionsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_update_slo_target_error_component import (
        ApiV1ConditionsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_conditions_update_target_availability_error_component import (
        ApiV1ConditionsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_update_tolerations_error_component import (
        ApiV1ConditionsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConditionsUpdateValidationError")


@_attrs_define
class ApiV1ConditionsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConditionsUpdateAnnotationsErrorComponent | ApiV1ConditionsUpdateArchivedAtErrorComponent |
            ApiV1ConditionsUpdateArchivedErrorComponent | ApiV1ConditionsUpdateArchivedReasonErrorComponent |
            ApiV1ConditionsUpdateCriticalityErrorComponent | ApiV1ConditionsUpdateDebugModeErrorComponent |
            ApiV1ConditionsUpdateDescriptionErrorComponent | ApiV1ConditionsUpdateDisplayNameErrorComponent |
            ApiV1ConditionsUpdateIsSystemErrorComponent | ApiV1ConditionsUpdateKindErrorComponent |
            ApiV1ConditionsUpdateLabelsErrorComponent | ApiV1ConditionsUpdateNameErrorComponent |
            ApiV1ConditionsUpdateNonFieldErrorsErrorComponent | ApiV1ConditionsUpdatePlatformServiceErrorComponent |
            ApiV1ConditionsUpdateProviderErrorComponent | ApiV1ConditionsUpdateProviderIdErrorComponent |
            ApiV1ConditionsUpdateProviderReferenceErrorComponent | ApiV1ConditionsUpdateReconciliationEnabledErrorComponent
            | ApiV1ConditionsUpdateSeverityErrorComponent | ApiV1ConditionsUpdateSlaAvailabilityErrorComponent |
            ApiV1ConditionsUpdateSlaTargetErrorComponent | ApiV1ConditionsUpdateSloAvailabilityErrorComponent |
            ApiV1ConditionsUpdateSloTargetErrorComponent | ApiV1ConditionsUpdateTargetAvailabilityErrorComponent |
            ApiV1ConditionsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConditionsUpdateAnnotationsErrorComponent
        | ApiV1ConditionsUpdateArchivedAtErrorComponent
        | ApiV1ConditionsUpdateArchivedErrorComponent
        | ApiV1ConditionsUpdateArchivedReasonErrorComponent
        | ApiV1ConditionsUpdateCriticalityErrorComponent
        | ApiV1ConditionsUpdateDebugModeErrorComponent
        | ApiV1ConditionsUpdateDescriptionErrorComponent
        | ApiV1ConditionsUpdateDisplayNameErrorComponent
        | ApiV1ConditionsUpdateIsSystemErrorComponent
        | ApiV1ConditionsUpdateKindErrorComponent
        | ApiV1ConditionsUpdateLabelsErrorComponent
        | ApiV1ConditionsUpdateNameErrorComponent
        | ApiV1ConditionsUpdateNonFieldErrorsErrorComponent
        | ApiV1ConditionsUpdatePlatformServiceErrorComponent
        | ApiV1ConditionsUpdateProviderErrorComponent
        | ApiV1ConditionsUpdateProviderIdErrorComponent
        | ApiV1ConditionsUpdateProviderReferenceErrorComponent
        | ApiV1ConditionsUpdateReconciliationEnabledErrorComponent
        | ApiV1ConditionsUpdateSeverityErrorComponent
        | ApiV1ConditionsUpdateSlaAvailabilityErrorComponent
        | ApiV1ConditionsUpdateSlaTargetErrorComponent
        | ApiV1ConditionsUpdateSloAvailabilityErrorComponent
        | ApiV1ConditionsUpdateSloTargetErrorComponent
        | ApiV1ConditionsUpdateTargetAvailabilityErrorComponent
        | ApiV1ConditionsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conditions_update_annotations_error_component import (
            ApiV1ConditionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_conditions_update_archived_at_error_component import (
            ApiV1ConditionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_conditions_update_archived_error_component import (
            ApiV1ConditionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_conditions_update_archived_reason_error_component import (
            ApiV1ConditionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_conditions_update_criticality_error_component import (
            ApiV1ConditionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_conditions_update_debug_mode_error_component import (
            ApiV1ConditionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_conditions_update_display_name_error_component import (
            ApiV1ConditionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_conditions_update_is_system_error_component import (
            ApiV1ConditionsUpdateIsSystemErrorComponent,
        )
        from ..models.api_v1_conditions_update_kind_error_component import ApiV1ConditionsUpdateKindErrorComponent
        from ..models.api_v1_conditions_update_labels_error_component import ApiV1ConditionsUpdateLabelsErrorComponent
        from ..models.api_v1_conditions_update_name_error_component import ApiV1ConditionsUpdateNameErrorComponent
        from ..models.api_v1_conditions_update_non_field_errors_error_component import (
            ApiV1ConditionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_conditions_update_platform_service_error_component import (
            ApiV1ConditionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_conditions_update_provider_error_component import (
            ApiV1ConditionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_conditions_update_provider_id_error_component import (
            ApiV1ConditionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_conditions_update_provider_reference_error_component import (
            ApiV1ConditionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_conditions_update_reconciliation_enabled_error_component import (
            ApiV1ConditionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_conditions_update_severity_error_component import (
            ApiV1ConditionsUpdateSeverityErrorComponent,
        )
        from ..models.api_v1_conditions_update_sla_availability_error_component import (
            ApiV1ConditionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_update_sla_target_error_component import (
            ApiV1ConditionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_conditions_update_slo_availability_error_component import (
            ApiV1ConditionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_update_slo_target_error_component import (
            ApiV1ConditionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_conditions_update_target_availability_error_component import (
            ApiV1ConditionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_update_tolerations_error_component import (
            ApiV1ConditionsUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConditionsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsUpdateIsSystemErrorComponent):
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
        from ..models.api_v1_conditions_update_annotations_error_component import (
            ApiV1ConditionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_conditions_update_archived_at_error_component import (
            ApiV1ConditionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_conditions_update_archived_error_component import (
            ApiV1ConditionsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_conditions_update_archived_reason_error_component import (
            ApiV1ConditionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_conditions_update_criticality_error_component import (
            ApiV1ConditionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_conditions_update_debug_mode_error_component import (
            ApiV1ConditionsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_conditions_update_description_error_component import (
            ApiV1ConditionsUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_conditions_update_display_name_error_component import (
            ApiV1ConditionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_conditions_update_is_system_error_component import (
            ApiV1ConditionsUpdateIsSystemErrorComponent,
        )
        from ..models.api_v1_conditions_update_kind_error_component import ApiV1ConditionsUpdateKindErrorComponent
        from ..models.api_v1_conditions_update_labels_error_component import ApiV1ConditionsUpdateLabelsErrorComponent
        from ..models.api_v1_conditions_update_name_error_component import ApiV1ConditionsUpdateNameErrorComponent
        from ..models.api_v1_conditions_update_non_field_errors_error_component import (
            ApiV1ConditionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_conditions_update_platform_service_error_component import (
            ApiV1ConditionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_conditions_update_provider_error_component import (
            ApiV1ConditionsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_conditions_update_provider_id_error_component import (
            ApiV1ConditionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_conditions_update_provider_reference_error_component import (
            ApiV1ConditionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_conditions_update_reconciliation_enabled_error_component import (
            ApiV1ConditionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_conditions_update_severity_error_component import (
            ApiV1ConditionsUpdateSeverityErrorComponent,
        )
        from ..models.api_v1_conditions_update_sla_availability_error_component import (
            ApiV1ConditionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_update_sla_target_error_component import (
            ApiV1ConditionsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_conditions_update_slo_availability_error_component import (
            ApiV1ConditionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_update_slo_target_error_component import (
            ApiV1ConditionsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_conditions_update_target_availability_error_component import (
            ApiV1ConditionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_update_tolerations_error_component import (
            ApiV1ConditionsUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConditionsUpdateAnnotationsErrorComponent
                | ApiV1ConditionsUpdateArchivedAtErrorComponent
                | ApiV1ConditionsUpdateArchivedErrorComponent
                | ApiV1ConditionsUpdateArchivedReasonErrorComponent
                | ApiV1ConditionsUpdateCriticalityErrorComponent
                | ApiV1ConditionsUpdateDebugModeErrorComponent
                | ApiV1ConditionsUpdateDescriptionErrorComponent
                | ApiV1ConditionsUpdateDisplayNameErrorComponent
                | ApiV1ConditionsUpdateIsSystemErrorComponent
                | ApiV1ConditionsUpdateKindErrorComponent
                | ApiV1ConditionsUpdateLabelsErrorComponent
                | ApiV1ConditionsUpdateNameErrorComponent
                | ApiV1ConditionsUpdateNonFieldErrorsErrorComponent
                | ApiV1ConditionsUpdatePlatformServiceErrorComponent
                | ApiV1ConditionsUpdateProviderErrorComponent
                | ApiV1ConditionsUpdateProviderIdErrorComponent
                | ApiV1ConditionsUpdateProviderReferenceErrorComponent
                | ApiV1ConditionsUpdateReconciliationEnabledErrorComponent
                | ApiV1ConditionsUpdateSeverityErrorComponent
                | ApiV1ConditionsUpdateSlaAvailabilityErrorComponent
                | ApiV1ConditionsUpdateSlaTargetErrorComponent
                | ApiV1ConditionsUpdateSloAvailabilityErrorComponent
                | ApiV1ConditionsUpdateSloTargetErrorComponent
                | ApiV1ConditionsUpdateTargetAvailabilityErrorComponent
                | ApiV1ConditionsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_0 = (
                        ApiV1ConditionsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_1 = (
                        ApiV1ConditionsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_2 = (
                        ApiV1ConditionsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_3 = (
                        ApiV1ConditionsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_4 = (
                        ApiV1ConditionsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_5 = (
                        ApiV1ConditionsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_6 = (
                        ApiV1ConditionsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_7 = (
                        ApiV1ConditionsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_8 = (
                        ApiV1ConditionsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_9 = (
                        ApiV1ConditionsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_10 = (
                        ApiV1ConditionsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_11 = (
                        ApiV1ConditionsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_12 = (
                        ApiV1ConditionsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_13 = (
                        ApiV1ConditionsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_14 = (
                        ApiV1ConditionsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_15 = (
                        ApiV1ConditionsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_16 = (
                        ApiV1ConditionsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_17 = (
                        ApiV1ConditionsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_18 = (
                        ApiV1ConditionsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_19 = (
                        ApiV1ConditionsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_20 = (
                        ApiV1ConditionsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_21 = (
                        ApiV1ConditionsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_22 = (
                        ApiV1ConditionsUpdateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_update_error_type_23 = (
                        ApiV1ConditionsUpdateIsSystemErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conditions_update_error_type_24 = (
                    ApiV1ConditionsUpdateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conditions_update_error_type_24

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conditions_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conditions_update_validation_error.additional_properties = d
        return api_v1_conditions_update_validation_error

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
