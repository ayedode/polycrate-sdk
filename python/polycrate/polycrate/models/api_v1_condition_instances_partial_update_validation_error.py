from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_condition_instances_partial_update_active_error_component import (
        ApiV1ConditionInstancesPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_annotations_error_component import (
        ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_archived_at_error_component import (
        ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_archived_error_component import (
        ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_archived_reason_error_component import (
        ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_condition_error_component import (
        ApiV1ConditionInstancesPartialUpdateConditionErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_context_error_component import (
        ApiV1ConditionInstancesPartialUpdateContextErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_criticality_error_component import (
        ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_debug_mode_error_component import (
        ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_display_name_error_component import (
        ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_immediate_error_component import (
        ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_kind_error_component import (
        ApiV1ConditionInstancesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_labels_error_component import (
        ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_name_error_component import (
        ApiV1ConditionInstancesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_non_field_errors_error_component import (
        ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_object_id_error_component import (
        ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_platform_service_error_component import (
        ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_provider_error_component import (
        ApiV1ConditionInstancesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_provider_id_error_component import (
        ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_provider_reference_error_component import (
        ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_reason_error_component import (
        ApiV1ConditionInstancesPartialUpdateReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_reconciliation_enabled_error_component import (
        ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_resolved_at_error_component import (
        ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_sla_availability_error_component import (
        ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_sla_target_error_component import (
        ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_slo_availability_error_component import (
        ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_slo_target_error_component import (
        ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_target_availability_error_component import (
        ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_partial_update_tolerations_error_component import (
        ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConditionInstancesPartialUpdateValidationError")


@_attrs_define
class ApiV1ConditionInstancesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConditionInstancesPartialUpdateActiveErrorComponent |
            ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent |
            ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent |
            ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent |
            ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent |
            ApiV1ConditionInstancesPartialUpdateConditionErrorComponent |
            ApiV1ConditionInstancesPartialUpdateContextErrorComponent |
            ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent |
            ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent |
            ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent |
            ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent |
            ApiV1ConditionInstancesPartialUpdateKindErrorComponent |
            ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent |
            ApiV1ConditionInstancesPartialUpdateNameErrorComponent |
            ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent |
            ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent |
            ApiV1ConditionInstancesPartialUpdateProviderErrorComponent |
            ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent |
            ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent |
            ApiV1ConditionInstancesPartialUpdateReasonErrorComponent |
            ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponent |
            ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent |
            ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent |
            ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConditionInstancesPartialUpdateActiveErrorComponent
        | ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent
        | ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent
        | ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent
        | ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent
        | ApiV1ConditionInstancesPartialUpdateConditionErrorComponent
        | ApiV1ConditionInstancesPartialUpdateContextErrorComponent
        | ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent
        | ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent
        | ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent
        | ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent
        | ApiV1ConditionInstancesPartialUpdateKindErrorComponent
        | ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent
        | ApiV1ConditionInstancesPartialUpdateNameErrorComponent
        | ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent
        | ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent
        | ApiV1ConditionInstancesPartialUpdateProviderErrorComponent
        | ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent
        | ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent
        | ApiV1ConditionInstancesPartialUpdateReasonErrorComponent
        | ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponent
        | ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent
        | ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent
        | ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_condition_instances_partial_update_active_error_component import (
            ApiV1ConditionInstancesPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_annotations_error_component import (
            ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_archived_at_error_component import (
            ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_archived_error_component import (
            ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_archived_reason_error_component import (
            ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_condition_error_component import (
            ApiV1ConditionInstancesPartialUpdateConditionErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_context_error_component import (
            ApiV1ConditionInstancesPartialUpdateContextErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_criticality_error_component import (
            ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_debug_mode_error_component import (
            ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_display_name_error_component import (
            ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_immediate_error_component import (
            ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_kind_error_component import (
            ApiV1ConditionInstancesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_labels_error_component import (
            ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_name_error_component import (
            ApiV1ConditionInstancesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_non_field_errors_error_component import (
            ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_object_id_error_component import (
            ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_platform_service_error_component import (
            ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_provider_error_component import (
            ApiV1ConditionInstancesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_provider_id_error_component import (
            ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_provider_reference_error_component import (
            ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_reason_error_component import (
            ApiV1ConditionInstancesPartialUpdateReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_sla_availability_error_component import (
            ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_sla_target_error_component import (
            ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_slo_availability_error_component import (
            ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_slo_target_error_component import (
            ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_target_availability_error_component import (
            ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_tolerations_error_component import (
            ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateConditionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateContextErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesPartialUpdateActiveErrorComponent):
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
        from ..models.api_v1_condition_instances_partial_update_active_error_component import (
            ApiV1ConditionInstancesPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_annotations_error_component import (
            ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_archived_at_error_component import (
            ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_archived_error_component import (
            ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_archived_reason_error_component import (
            ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_condition_error_component import (
            ApiV1ConditionInstancesPartialUpdateConditionErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_context_error_component import (
            ApiV1ConditionInstancesPartialUpdateContextErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_criticality_error_component import (
            ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_debug_mode_error_component import (
            ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_display_name_error_component import (
            ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_immediate_error_component import (
            ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_kind_error_component import (
            ApiV1ConditionInstancesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_labels_error_component import (
            ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_name_error_component import (
            ApiV1ConditionInstancesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_non_field_errors_error_component import (
            ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_object_id_error_component import (
            ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_platform_service_error_component import (
            ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_provider_error_component import (
            ApiV1ConditionInstancesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_provider_id_error_component import (
            ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_provider_reference_error_component import (
            ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_reason_error_component import (
            ApiV1ConditionInstancesPartialUpdateReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_resolved_at_error_component import (
            ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_sla_availability_error_component import (
            ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_sla_target_error_component import (
            ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_slo_availability_error_component import (
            ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_slo_target_error_component import (
            ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_target_availability_error_component import (
            ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_partial_update_tolerations_error_component import (
            ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConditionInstancesPartialUpdateActiveErrorComponent
                | ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent
                | ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent
                | ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent
                | ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent
                | ApiV1ConditionInstancesPartialUpdateConditionErrorComponent
                | ApiV1ConditionInstancesPartialUpdateContextErrorComponent
                | ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent
                | ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent
                | ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent
                | ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent
                | ApiV1ConditionInstancesPartialUpdateKindErrorComponent
                | ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent
                | ApiV1ConditionInstancesPartialUpdateNameErrorComponent
                | ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent
                | ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent
                | ApiV1ConditionInstancesPartialUpdateProviderErrorComponent
                | ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent
                | ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent
                | ApiV1ConditionInstancesPartialUpdateReasonErrorComponent
                | ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponent
                | ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent
                | ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent
                | ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_0 = (
                        ApiV1ConditionInstancesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_1 = (
                        ApiV1ConditionInstancesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_2 = (
                        ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_3 = (
                        ApiV1ConditionInstancesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_4 = (
                        ApiV1ConditionInstancesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_5 = (
                        ApiV1ConditionInstancesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_6 = (
                        ApiV1ConditionInstancesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_7 = (
                        ApiV1ConditionInstancesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_8 = (
                        ApiV1ConditionInstancesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_9 = (
                        ApiV1ConditionInstancesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_10 = (
                        ApiV1ConditionInstancesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_11 = (
                        ApiV1ConditionInstancesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_12 = (
                        ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_13 = (
                        ApiV1ConditionInstancesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_14 = (
                        ApiV1ConditionInstancesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_15 = (
                        ApiV1ConditionInstancesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_16 = (
                        ApiV1ConditionInstancesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_17 = (
                        ApiV1ConditionInstancesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_18 = (
                        ApiV1ConditionInstancesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_19 = (
                        ApiV1ConditionInstancesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_20 = (
                        ApiV1ConditionInstancesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_21 = (
                        ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_22 = (
                        ApiV1ConditionInstancesPartialUpdateConditionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_23 = (
                        ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_24 = (
                        ApiV1ConditionInstancesPartialUpdateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_25 = (
                        ApiV1ConditionInstancesPartialUpdateContextErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_26 = (
                        ApiV1ConditionInstancesPartialUpdateImmediateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_partial_update_error_type_27 = (
                        ApiV1ConditionInstancesPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_condition_instances_partial_update_error_type_28 = (
                    ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_condition_instances_partial_update_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_condition_instances_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_condition_instances_partial_update_validation_error.additional_properties = d
        return api_v1_condition_instances_partial_update_validation_error

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
