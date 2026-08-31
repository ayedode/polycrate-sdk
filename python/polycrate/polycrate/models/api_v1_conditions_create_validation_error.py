from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_conditions_create_annotations_error_component import (
        ApiV1ConditionsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_conditions_create_archived_at_error_component import (
        ApiV1ConditionsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_conditions_create_archived_error_component import ApiV1ConditionsCreateArchivedErrorComponent
    from ..models.api_v1_conditions_create_archived_reason_error_component import (
        ApiV1ConditionsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_conditions_create_criticality_error_component import (
        ApiV1ConditionsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_conditions_create_debug_mode_error_component import (
        ApiV1ConditionsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_conditions_create_description_error_component import (
        ApiV1ConditionsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_conditions_create_display_name_error_component import (
        ApiV1ConditionsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_conditions_create_is_system_error_component import ApiV1ConditionsCreateIsSystemErrorComponent
    from ..models.api_v1_conditions_create_kind_error_component import ApiV1ConditionsCreateKindErrorComponent
    from ..models.api_v1_conditions_create_labels_error_component import ApiV1ConditionsCreateLabelsErrorComponent
    from ..models.api_v1_conditions_create_name_error_component import ApiV1ConditionsCreateNameErrorComponent
    from ..models.api_v1_conditions_create_non_field_errors_error_component import (
        ApiV1ConditionsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_conditions_create_platform_service_error_component import (
        ApiV1ConditionsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_conditions_create_provider_error_component import ApiV1ConditionsCreateProviderErrorComponent
    from ..models.api_v1_conditions_create_provider_id_error_component import (
        ApiV1ConditionsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_conditions_create_provider_reference_error_component import (
        ApiV1ConditionsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_conditions_create_reconciliation_enabled_error_component import (
        ApiV1ConditionsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_conditions_create_severity_error_component import ApiV1ConditionsCreateSeverityErrorComponent
    from ..models.api_v1_conditions_create_sla_availability_error_component import (
        ApiV1ConditionsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_create_sla_target_error_component import (
        ApiV1ConditionsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_conditions_create_slo_availability_error_component import (
        ApiV1ConditionsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_create_slo_target_error_component import (
        ApiV1ConditionsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_conditions_create_target_availability_error_component import (
        ApiV1ConditionsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_conditions_create_tolerations_error_component import (
        ApiV1ConditionsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConditionsCreateValidationError")


@_attrs_define
class ApiV1ConditionsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConditionsCreateAnnotationsErrorComponent | ApiV1ConditionsCreateArchivedAtErrorComponent |
            ApiV1ConditionsCreateArchivedErrorComponent | ApiV1ConditionsCreateArchivedReasonErrorComponent |
            ApiV1ConditionsCreateCriticalityErrorComponent | ApiV1ConditionsCreateDebugModeErrorComponent |
            ApiV1ConditionsCreateDescriptionErrorComponent | ApiV1ConditionsCreateDisplayNameErrorComponent |
            ApiV1ConditionsCreateIsSystemErrorComponent | ApiV1ConditionsCreateKindErrorComponent |
            ApiV1ConditionsCreateLabelsErrorComponent | ApiV1ConditionsCreateNameErrorComponent |
            ApiV1ConditionsCreateNonFieldErrorsErrorComponent | ApiV1ConditionsCreatePlatformServiceErrorComponent |
            ApiV1ConditionsCreateProviderErrorComponent | ApiV1ConditionsCreateProviderIdErrorComponent |
            ApiV1ConditionsCreateProviderReferenceErrorComponent | ApiV1ConditionsCreateReconciliationEnabledErrorComponent
            | ApiV1ConditionsCreateSeverityErrorComponent | ApiV1ConditionsCreateSlaAvailabilityErrorComponent |
            ApiV1ConditionsCreateSlaTargetErrorComponent | ApiV1ConditionsCreateSloAvailabilityErrorComponent |
            ApiV1ConditionsCreateSloTargetErrorComponent | ApiV1ConditionsCreateTargetAvailabilityErrorComponent |
            ApiV1ConditionsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConditionsCreateAnnotationsErrorComponent
        | ApiV1ConditionsCreateArchivedAtErrorComponent
        | ApiV1ConditionsCreateArchivedErrorComponent
        | ApiV1ConditionsCreateArchivedReasonErrorComponent
        | ApiV1ConditionsCreateCriticalityErrorComponent
        | ApiV1ConditionsCreateDebugModeErrorComponent
        | ApiV1ConditionsCreateDescriptionErrorComponent
        | ApiV1ConditionsCreateDisplayNameErrorComponent
        | ApiV1ConditionsCreateIsSystemErrorComponent
        | ApiV1ConditionsCreateKindErrorComponent
        | ApiV1ConditionsCreateLabelsErrorComponent
        | ApiV1ConditionsCreateNameErrorComponent
        | ApiV1ConditionsCreateNonFieldErrorsErrorComponent
        | ApiV1ConditionsCreatePlatformServiceErrorComponent
        | ApiV1ConditionsCreateProviderErrorComponent
        | ApiV1ConditionsCreateProviderIdErrorComponent
        | ApiV1ConditionsCreateProviderReferenceErrorComponent
        | ApiV1ConditionsCreateReconciliationEnabledErrorComponent
        | ApiV1ConditionsCreateSeverityErrorComponent
        | ApiV1ConditionsCreateSlaAvailabilityErrorComponent
        | ApiV1ConditionsCreateSlaTargetErrorComponent
        | ApiV1ConditionsCreateSloAvailabilityErrorComponent
        | ApiV1ConditionsCreateSloTargetErrorComponent
        | ApiV1ConditionsCreateTargetAvailabilityErrorComponent
        | ApiV1ConditionsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_conditions_create_annotations_error_component import (
            ApiV1ConditionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_conditions_create_archived_at_error_component import (
            ApiV1ConditionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_conditions_create_archived_error_component import (
            ApiV1ConditionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_conditions_create_archived_reason_error_component import (
            ApiV1ConditionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_conditions_create_criticality_error_component import (
            ApiV1ConditionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_conditions_create_debug_mode_error_component import (
            ApiV1ConditionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_conditions_create_display_name_error_component import (
            ApiV1ConditionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_conditions_create_is_system_error_component import (
            ApiV1ConditionsCreateIsSystemErrorComponent,
        )
        from ..models.api_v1_conditions_create_kind_error_component import ApiV1ConditionsCreateKindErrorComponent
        from ..models.api_v1_conditions_create_labels_error_component import ApiV1ConditionsCreateLabelsErrorComponent
        from ..models.api_v1_conditions_create_name_error_component import ApiV1ConditionsCreateNameErrorComponent
        from ..models.api_v1_conditions_create_non_field_errors_error_component import (
            ApiV1ConditionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_conditions_create_platform_service_error_component import (
            ApiV1ConditionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_conditions_create_provider_error_component import (
            ApiV1ConditionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_conditions_create_provider_id_error_component import (
            ApiV1ConditionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_conditions_create_provider_reference_error_component import (
            ApiV1ConditionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_conditions_create_reconciliation_enabled_error_component import (
            ApiV1ConditionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_conditions_create_severity_error_component import (
            ApiV1ConditionsCreateSeverityErrorComponent,
        )
        from ..models.api_v1_conditions_create_sla_availability_error_component import (
            ApiV1ConditionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_create_sla_target_error_component import (
            ApiV1ConditionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_conditions_create_slo_availability_error_component import (
            ApiV1ConditionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_create_slo_target_error_component import (
            ApiV1ConditionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_conditions_create_target_availability_error_component import (
            ApiV1ConditionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_create_tolerations_error_component import (
            ApiV1ConditionsCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConditionsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionsCreateIsSystemErrorComponent):
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
        from ..models.api_v1_conditions_create_annotations_error_component import (
            ApiV1ConditionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_conditions_create_archived_at_error_component import (
            ApiV1ConditionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_conditions_create_archived_error_component import (
            ApiV1ConditionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_conditions_create_archived_reason_error_component import (
            ApiV1ConditionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_conditions_create_criticality_error_component import (
            ApiV1ConditionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_conditions_create_debug_mode_error_component import (
            ApiV1ConditionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_conditions_create_description_error_component import (
            ApiV1ConditionsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_conditions_create_display_name_error_component import (
            ApiV1ConditionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_conditions_create_is_system_error_component import (
            ApiV1ConditionsCreateIsSystemErrorComponent,
        )
        from ..models.api_v1_conditions_create_kind_error_component import ApiV1ConditionsCreateKindErrorComponent
        from ..models.api_v1_conditions_create_labels_error_component import ApiV1ConditionsCreateLabelsErrorComponent
        from ..models.api_v1_conditions_create_name_error_component import ApiV1ConditionsCreateNameErrorComponent
        from ..models.api_v1_conditions_create_non_field_errors_error_component import (
            ApiV1ConditionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_conditions_create_platform_service_error_component import (
            ApiV1ConditionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_conditions_create_provider_error_component import (
            ApiV1ConditionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_conditions_create_provider_id_error_component import (
            ApiV1ConditionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_conditions_create_provider_reference_error_component import (
            ApiV1ConditionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_conditions_create_reconciliation_enabled_error_component import (
            ApiV1ConditionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_conditions_create_severity_error_component import (
            ApiV1ConditionsCreateSeverityErrorComponent,
        )
        from ..models.api_v1_conditions_create_sla_availability_error_component import (
            ApiV1ConditionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_create_sla_target_error_component import (
            ApiV1ConditionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_conditions_create_slo_availability_error_component import (
            ApiV1ConditionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_create_slo_target_error_component import (
            ApiV1ConditionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_conditions_create_target_availability_error_component import (
            ApiV1ConditionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_conditions_create_tolerations_error_component import (
            ApiV1ConditionsCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConditionsCreateAnnotationsErrorComponent
                | ApiV1ConditionsCreateArchivedAtErrorComponent
                | ApiV1ConditionsCreateArchivedErrorComponent
                | ApiV1ConditionsCreateArchivedReasonErrorComponent
                | ApiV1ConditionsCreateCriticalityErrorComponent
                | ApiV1ConditionsCreateDebugModeErrorComponent
                | ApiV1ConditionsCreateDescriptionErrorComponent
                | ApiV1ConditionsCreateDisplayNameErrorComponent
                | ApiV1ConditionsCreateIsSystemErrorComponent
                | ApiV1ConditionsCreateKindErrorComponent
                | ApiV1ConditionsCreateLabelsErrorComponent
                | ApiV1ConditionsCreateNameErrorComponent
                | ApiV1ConditionsCreateNonFieldErrorsErrorComponent
                | ApiV1ConditionsCreatePlatformServiceErrorComponent
                | ApiV1ConditionsCreateProviderErrorComponent
                | ApiV1ConditionsCreateProviderIdErrorComponent
                | ApiV1ConditionsCreateProviderReferenceErrorComponent
                | ApiV1ConditionsCreateReconciliationEnabledErrorComponent
                | ApiV1ConditionsCreateSeverityErrorComponent
                | ApiV1ConditionsCreateSlaAvailabilityErrorComponent
                | ApiV1ConditionsCreateSlaTargetErrorComponent
                | ApiV1ConditionsCreateSloAvailabilityErrorComponent
                | ApiV1ConditionsCreateSloTargetErrorComponent
                | ApiV1ConditionsCreateTargetAvailabilityErrorComponent
                | ApiV1ConditionsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_0 = (
                        ApiV1ConditionsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_1 = (
                        ApiV1ConditionsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_2 = (
                        ApiV1ConditionsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_3 = (
                        ApiV1ConditionsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_4 = (
                        ApiV1ConditionsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_5 = (
                        ApiV1ConditionsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_6 = (
                        ApiV1ConditionsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_7 = (
                        ApiV1ConditionsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_8 = (
                        ApiV1ConditionsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_9 = (
                        ApiV1ConditionsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_10 = (
                        ApiV1ConditionsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_11 = (
                        ApiV1ConditionsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_12 = (
                        ApiV1ConditionsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_13 = (
                        ApiV1ConditionsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_14 = (
                        ApiV1ConditionsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_15 = (
                        ApiV1ConditionsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_16 = (
                        ApiV1ConditionsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_17 = (
                        ApiV1ConditionsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_18 = (
                        ApiV1ConditionsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_19 = (
                        ApiV1ConditionsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_20 = (
                        ApiV1ConditionsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_21 = (
                        ApiV1ConditionsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_22 = (
                        ApiV1ConditionsCreateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_conditions_create_error_type_23 = (
                        ApiV1ConditionsCreateIsSystemErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_conditions_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conditions_create_error_type_24 = (
                    ApiV1ConditionsCreateDescriptionErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_conditions_create_error_type_24

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_conditions_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_conditions_create_validation_error.additional_properties = d
        return api_v1_conditions_create_validation_error

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
