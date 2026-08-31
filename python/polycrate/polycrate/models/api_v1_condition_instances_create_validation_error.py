from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_condition_instances_create_active_error_component import (
        ApiV1ConditionInstancesCreateActiveErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_annotations_error_component import (
        ApiV1ConditionInstancesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_archived_at_error_component import (
        ApiV1ConditionInstancesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_archived_error_component import (
        ApiV1ConditionInstancesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_archived_reason_error_component import (
        ApiV1ConditionInstancesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_condition_error_component import (
        ApiV1ConditionInstancesCreateConditionErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_context_error_component import (
        ApiV1ConditionInstancesCreateContextErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_criticality_error_component import (
        ApiV1ConditionInstancesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_debug_mode_error_component import (
        ApiV1ConditionInstancesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_display_name_error_component import (
        ApiV1ConditionInstancesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_immediate_error_component import (
        ApiV1ConditionInstancesCreateImmediateErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_kind_error_component import (
        ApiV1ConditionInstancesCreateKindErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_labels_error_component import (
        ApiV1ConditionInstancesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_name_error_component import (
        ApiV1ConditionInstancesCreateNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_non_field_errors_error_component import (
        ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_object_id_error_component import (
        ApiV1ConditionInstancesCreateObjectIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_platform_service_error_component import (
        ApiV1ConditionInstancesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_provider_error_component import (
        ApiV1ConditionInstancesCreateProviderErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_provider_id_error_component import (
        ApiV1ConditionInstancesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_provider_reference_error_component import (
        ApiV1ConditionInstancesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_reason_error_component import (
        ApiV1ConditionInstancesCreateReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_reconciliation_enabled_error_component import (
        ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_resolved_at_error_component import (
        ApiV1ConditionInstancesCreateResolvedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_sla_availability_error_component import (
        ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_sla_target_error_component import (
        ApiV1ConditionInstancesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_slo_availability_error_component import (
        ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_slo_target_error_component import (
        ApiV1ConditionInstancesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_target_availability_error_component import (
        ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_create_tolerations_error_component import (
        ApiV1ConditionInstancesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConditionInstancesCreateValidationError")


@_attrs_define
class ApiV1ConditionInstancesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConditionInstancesCreateActiveErrorComponent |
            ApiV1ConditionInstancesCreateAnnotationsErrorComponent | ApiV1ConditionInstancesCreateArchivedAtErrorComponent |
            ApiV1ConditionInstancesCreateArchivedErrorComponent | ApiV1ConditionInstancesCreateArchivedReasonErrorComponent
            | ApiV1ConditionInstancesCreateConditionErrorComponent | ApiV1ConditionInstancesCreateContextErrorComponent |
            ApiV1ConditionInstancesCreateCriticalityErrorComponent | ApiV1ConditionInstancesCreateDebugModeErrorComponent |
            ApiV1ConditionInstancesCreateDisplayNameErrorComponent | ApiV1ConditionInstancesCreateImmediateErrorComponent |
            ApiV1ConditionInstancesCreateKindErrorComponent | ApiV1ConditionInstancesCreateLabelsErrorComponent |
            ApiV1ConditionInstancesCreateNameErrorComponent | ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent |
            ApiV1ConditionInstancesCreateObjectIdErrorComponent | ApiV1ConditionInstancesCreatePlatformServiceErrorComponent
            | ApiV1ConditionInstancesCreateProviderErrorComponent | ApiV1ConditionInstancesCreateProviderIdErrorComponent |
            ApiV1ConditionInstancesCreateProviderReferenceErrorComponent | ApiV1ConditionInstancesCreateReasonErrorComponent
            | ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent |
            ApiV1ConditionInstancesCreateResolvedAtErrorComponent |
            ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent |
            ApiV1ConditionInstancesCreateSlaTargetErrorComponent |
            ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent |
            ApiV1ConditionInstancesCreateSloTargetErrorComponent |
            ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent |
            ApiV1ConditionInstancesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConditionInstancesCreateActiveErrorComponent
        | ApiV1ConditionInstancesCreateAnnotationsErrorComponent
        | ApiV1ConditionInstancesCreateArchivedAtErrorComponent
        | ApiV1ConditionInstancesCreateArchivedErrorComponent
        | ApiV1ConditionInstancesCreateArchivedReasonErrorComponent
        | ApiV1ConditionInstancesCreateConditionErrorComponent
        | ApiV1ConditionInstancesCreateContextErrorComponent
        | ApiV1ConditionInstancesCreateCriticalityErrorComponent
        | ApiV1ConditionInstancesCreateDebugModeErrorComponent
        | ApiV1ConditionInstancesCreateDisplayNameErrorComponent
        | ApiV1ConditionInstancesCreateImmediateErrorComponent
        | ApiV1ConditionInstancesCreateKindErrorComponent
        | ApiV1ConditionInstancesCreateLabelsErrorComponent
        | ApiV1ConditionInstancesCreateNameErrorComponent
        | ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent
        | ApiV1ConditionInstancesCreateObjectIdErrorComponent
        | ApiV1ConditionInstancesCreatePlatformServiceErrorComponent
        | ApiV1ConditionInstancesCreateProviderErrorComponent
        | ApiV1ConditionInstancesCreateProviderIdErrorComponent
        | ApiV1ConditionInstancesCreateProviderReferenceErrorComponent
        | ApiV1ConditionInstancesCreateReasonErrorComponent
        | ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent
        | ApiV1ConditionInstancesCreateResolvedAtErrorComponent
        | ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent
        | ApiV1ConditionInstancesCreateSlaTargetErrorComponent
        | ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent
        | ApiV1ConditionInstancesCreateSloTargetErrorComponent
        | ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent
        | ApiV1ConditionInstancesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_condition_instances_create_active_error_component import (
            ApiV1ConditionInstancesCreateActiveErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_annotations_error_component import (
            ApiV1ConditionInstancesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_archived_at_error_component import (
            ApiV1ConditionInstancesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_archived_error_component import (
            ApiV1ConditionInstancesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_archived_reason_error_component import (
            ApiV1ConditionInstancesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_condition_error_component import (
            ApiV1ConditionInstancesCreateConditionErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_context_error_component import (
            ApiV1ConditionInstancesCreateContextErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_criticality_error_component import (
            ApiV1ConditionInstancesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_debug_mode_error_component import (
            ApiV1ConditionInstancesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_display_name_error_component import (
            ApiV1ConditionInstancesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_immediate_error_component import (
            ApiV1ConditionInstancesCreateImmediateErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_kind_error_component import (
            ApiV1ConditionInstancesCreateKindErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_labels_error_component import (
            ApiV1ConditionInstancesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_name_error_component import (
            ApiV1ConditionInstancesCreateNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_non_field_errors_error_component import (
            ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_object_id_error_component import (
            ApiV1ConditionInstancesCreateObjectIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_platform_service_error_component import (
            ApiV1ConditionInstancesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_provider_error_component import (
            ApiV1ConditionInstancesCreateProviderErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_provider_id_error_component import (
            ApiV1ConditionInstancesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_provider_reference_error_component import (
            ApiV1ConditionInstancesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_reason_error_component import (
            ApiV1ConditionInstancesCreateReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_sla_availability_error_component import (
            ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_sla_target_error_component import (
            ApiV1ConditionInstancesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_slo_availability_error_component import (
            ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_slo_target_error_component import (
            ApiV1ConditionInstancesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_target_availability_error_component import (
            ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_tolerations_error_component import (
            ApiV1ConditionInstancesCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateConditionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateContextErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateImmediateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesCreateActiveErrorComponent):
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
        from ..models.api_v1_condition_instances_create_active_error_component import (
            ApiV1ConditionInstancesCreateActiveErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_annotations_error_component import (
            ApiV1ConditionInstancesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_archived_at_error_component import (
            ApiV1ConditionInstancesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_archived_error_component import (
            ApiV1ConditionInstancesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_archived_reason_error_component import (
            ApiV1ConditionInstancesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_condition_error_component import (
            ApiV1ConditionInstancesCreateConditionErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_context_error_component import (
            ApiV1ConditionInstancesCreateContextErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_criticality_error_component import (
            ApiV1ConditionInstancesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_debug_mode_error_component import (
            ApiV1ConditionInstancesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_display_name_error_component import (
            ApiV1ConditionInstancesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_immediate_error_component import (
            ApiV1ConditionInstancesCreateImmediateErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_kind_error_component import (
            ApiV1ConditionInstancesCreateKindErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_labels_error_component import (
            ApiV1ConditionInstancesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_name_error_component import (
            ApiV1ConditionInstancesCreateNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_non_field_errors_error_component import (
            ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_object_id_error_component import (
            ApiV1ConditionInstancesCreateObjectIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_platform_service_error_component import (
            ApiV1ConditionInstancesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_provider_error_component import (
            ApiV1ConditionInstancesCreateProviderErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_provider_id_error_component import (
            ApiV1ConditionInstancesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_provider_reference_error_component import (
            ApiV1ConditionInstancesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_reason_error_component import (
            ApiV1ConditionInstancesCreateReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_resolved_at_error_component import (
            ApiV1ConditionInstancesCreateResolvedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_sla_availability_error_component import (
            ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_sla_target_error_component import (
            ApiV1ConditionInstancesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_slo_availability_error_component import (
            ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_slo_target_error_component import (
            ApiV1ConditionInstancesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_target_availability_error_component import (
            ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_create_tolerations_error_component import (
            ApiV1ConditionInstancesCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConditionInstancesCreateActiveErrorComponent
                | ApiV1ConditionInstancesCreateAnnotationsErrorComponent
                | ApiV1ConditionInstancesCreateArchivedAtErrorComponent
                | ApiV1ConditionInstancesCreateArchivedErrorComponent
                | ApiV1ConditionInstancesCreateArchivedReasonErrorComponent
                | ApiV1ConditionInstancesCreateConditionErrorComponent
                | ApiV1ConditionInstancesCreateContextErrorComponent
                | ApiV1ConditionInstancesCreateCriticalityErrorComponent
                | ApiV1ConditionInstancesCreateDebugModeErrorComponent
                | ApiV1ConditionInstancesCreateDisplayNameErrorComponent
                | ApiV1ConditionInstancesCreateImmediateErrorComponent
                | ApiV1ConditionInstancesCreateKindErrorComponent
                | ApiV1ConditionInstancesCreateLabelsErrorComponent
                | ApiV1ConditionInstancesCreateNameErrorComponent
                | ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent
                | ApiV1ConditionInstancesCreateObjectIdErrorComponent
                | ApiV1ConditionInstancesCreatePlatformServiceErrorComponent
                | ApiV1ConditionInstancesCreateProviderErrorComponent
                | ApiV1ConditionInstancesCreateProviderIdErrorComponent
                | ApiV1ConditionInstancesCreateProviderReferenceErrorComponent
                | ApiV1ConditionInstancesCreateReasonErrorComponent
                | ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent
                | ApiV1ConditionInstancesCreateResolvedAtErrorComponent
                | ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent
                | ApiV1ConditionInstancesCreateSlaTargetErrorComponent
                | ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent
                | ApiV1ConditionInstancesCreateSloTargetErrorComponent
                | ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent
                | ApiV1ConditionInstancesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_0 = (
                        ApiV1ConditionInstancesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_1 = (
                        ApiV1ConditionInstancesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_2 = (
                        ApiV1ConditionInstancesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_3 = (
                        ApiV1ConditionInstancesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_4 = (
                        ApiV1ConditionInstancesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_5 = (
                        ApiV1ConditionInstancesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_6 = (
                        ApiV1ConditionInstancesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_7 = (
                        ApiV1ConditionInstancesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_8 = (
                        ApiV1ConditionInstancesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_9 = (
                        ApiV1ConditionInstancesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_10 = (
                        ApiV1ConditionInstancesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_11 = (
                        ApiV1ConditionInstancesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_12 = (
                        ApiV1ConditionInstancesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_13 = (
                        ApiV1ConditionInstancesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_14 = (
                        ApiV1ConditionInstancesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_15 = (
                        ApiV1ConditionInstancesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_16 = (
                        ApiV1ConditionInstancesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_17 = (
                        ApiV1ConditionInstancesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_18 = (
                        ApiV1ConditionInstancesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_19 = (
                        ApiV1ConditionInstancesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_20 = (
                        ApiV1ConditionInstancesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_21 = (
                        ApiV1ConditionInstancesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_22 = (
                        ApiV1ConditionInstancesCreateConditionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_23 = (
                        ApiV1ConditionInstancesCreateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_24 = (
                        ApiV1ConditionInstancesCreateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_25 = (
                        ApiV1ConditionInstancesCreateContextErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_26 = (
                        ApiV1ConditionInstancesCreateImmediateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_create_error_type_27 = (
                        ApiV1ConditionInstancesCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_condition_instances_create_error_type_28 = (
                    ApiV1ConditionInstancesCreateResolvedAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_condition_instances_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_condition_instances_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_condition_instances_create_validation_error.additional_properties = d
        return api_v1_condition_instances_create_validation_error

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
