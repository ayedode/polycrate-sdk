from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_condition_instances_update_active_error_component import (
        ApiV1ConditionInstancesUpdateActiveErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_annotations_error_component import (
        ApiV1ConditionInstancesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_archived_at_error_component import (
        ApiV1ConditionInstancesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_archived_error_component import (
        ApiV1ConditionInstancesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_archived_reason_error_component import (
        ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_condition_error_component import (
        ApiV1ConditionInstancesUpdateConditionErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_context_error_component import (
        ApiV1ConditionInstancesUpdateContextErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_criticality_error_component import (
        ApiV1ConditionInstancesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_debug_mode_error_component import (
        ApiV1ConditionInstancesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_display_name_error_component import (
        ApiV1ConditionInstancesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_immediate_error_component import (
        ApiV1ConditionInstancesUpdateImmediateErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_kind_error_component import (
        ApiV1ConditionInstancesUpdateKindErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_labels_error_component import (
        ApiV1ConditionInstancesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_name_error_component import (
        ApiV1ConditionInstancesUpdateNameErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_non_field_errors_error_component import (
        ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_object_id_error_component import (
        ApiV1ConditionInstancesUpdateObjectIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_platform_service_error_component import (
        ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_provider_error_component import (
        ApiV1ConditionInstancesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_provider_id_error_component import (
        ApiV1ConditionInstancesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_provider_reference_error_component import (
        ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_reason_error_component import (
        ApiV1ConditionInstancesUpdateReasonErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_reconciliation_enabled_error_component import (
        ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_resolved_at_error_component import (
        ApiV1ConditionInstancesUpdateResolvedAtErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_sla_availability_error_component import (
        ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_sla_target_error_component import (
        ApiV1ConditionInstancesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_slo_availability_error_component import (
        ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_slo_target_error_component import (
        ApiV1ConditionInstancesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_target_availability_error_component import (
        ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_condition_instances_update_tolerations_error_component import (
        ApiV1ConditionInstancesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ConditionInstancesUpdateValidationError")


@_attrs_define
class ApiV1ConditionInstancesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ConditionInstancesUpdateActiveErrorComponent |
            ApiV1ConditionInstancesUpdateAnnotationsErrorComponent | ApiV1ConditionInstancesUpdateArchivedAtErrorComponent |
            ApiV1ConditionInstancesUpdateArchivedErrorComponent | ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent
            | ApiV1ConditionInstancesUpdateConditionErrorComponent | ApiV1ConditionInstancesUpdateContextErrorComponent |
            ApiV1ConditionInstancesUpdateCriticalityErrorComponent | ApiV1ConditionInstancesUpdateDebugModeErrorComponent |
            ApiV1ConditionInstancesUpdateDisplayNameErrorComponent | ApiV1ConditionInstancesUpdateImmediateErrorComponent |
            ApiV1ConditionInstancesUpdateKindErrorComponent | ApiV1ConditionInstancesUpdateLabelsErrorComponent |
            ApiV1ConditionInstancesUpdateNameErrorComponent | ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent |
            ApiV1ConditionInstancesUpdateObjectIdErrorComponent | ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent
            | ApiV1ConditionInstancesUpdateProviderErrorComponent | ApiV1ConditionInstancesUpdateProviderIdErrorComponent |
            ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent | ApiV1ConditionInstancesUpdateReasonErrorComponent
            | ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent |
            ApiV1ConditionInstancesUpdateResolvedAtErrorComponent |
            ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent |
            ApiV1ConditionInstancesUpdateSlaTargetErrorComponent |
            ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent |
            ApiV1ConditionInstancesUpdateSloTargetErrorComponent |
            ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent |
            ApiV1ConditionInstancesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ConditionInstancesUpdateActiveErrorComponent
        | ApiV1ConditionInstancesUpdateAnnotationsErrorComponent
        | ApiV1ConditionInstancesUpdateArchivedAtErrorComponent
        | ApiV1ConditionInstancesUpdateArchivedErrorComponent
        | ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent
        | ApiV1ConditionInstancesUpdateConditionErrorComponent
        | ApiV1ConditionInstancesUpdateContextErrorComponent
        | ApiV1ConditionInstancesUpdateCriticalityErrorComponent
        | ApiV1ConditionInstancesUpdateDebugModeErrorComponent
        | ApiV1ConditionInstancesUpdateDisplayNameErrorComponent
        | ApiV1ConditionInstancesUpdateImmediateErrorComponent
        | ApiV1ConditionInstancesUpdateKindErrorComponent
        | ApiV1ConditionInstancesUpdateLabelsErrorComponent
        | ApiV1ConditionInstancesUpdateNameErrorComponent
        | ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent
        | ApiV1ConditionInstancesUpdateObjectIdErrorComponent
        | ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent
        | ApiV1ConditionInstancesUpdateProviderErrorComponent
        | ApiV1ConditionInstancesUpdateProviderIdErrorComponent
        | ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent
        | ApiV1ConditionInstancesUpdateReasonErrorComponent
        | ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent
        | ApiV1ConditionInstancesUpdateResolvedAtErrorComponent
        | ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent
        | ApiV1ConditionInstancesUpdateSlaTargetErrorComponent
        | ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent
        | ApiV1ConditionInstancesUpdateSloTargetErrorComponent
        | ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent
        | ApiV1ConditionInstancesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_condition_instances_update_active_error_component import (
            ApiV1ConditionInstancesUpdateActiveErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_annotations_error_component import (
            ApiV1ConditionInstancesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_archived_at_error_component import (
            ApiV1ConditionInstancesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_archived_error_component import (
            ApiV1ConditionInstancesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_archived_reason_error_component import (
            ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_condition_error_component import (
            ApiV1ConditionInstancesUpdateConditionErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_context_error_component import (
            ApiV1ConditionInstancesUpdateContextErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_criticality_error_component import (
            ApiV1ConditionInstancesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_debug_mode_error_component import (
            ApiV1ConditionInstancesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_display_name_error_component import (
            ApiV1ConditionInstancesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_immediate_error_component import (
            ApiV1ConditionInstancesUpdateImmediateErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_kind_error_component import (
            ApiV1ConditionInstancesUpdateKindErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_labels_error_component import (
            ApiV1ConditionInstancesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_name_error_component import (
            ApiV1ConditionInstancesUpdateNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_non_field_errors_error_component import (
            ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_object_id_error_component import (
            ApiV1ConditionInstancesUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_platform_service_error_component import (
            ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_provider_error_component import (
            ApiV1ConditionInstancesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_provider_id_error_component import (
            ApiV1ConditionInstancesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_provider_reference_error_component import (
            ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_reason_error_component import (
            ApiV1ConditionInstancesUpdateReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_sla_availability_error_component import (
            ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_sla_target_error_component import (
            ApiV1ConditionInstancesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_slo_availability_error_component import (
            ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_slo_target_error_component import (
            ApiV1ConditionInstancesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_target_availability_error_component import (
            ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_tolerations_error_component import (
            ApiV1ConditionInstancesUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateConditionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateContextErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateImmediateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ConditionInstancesUpdateActiveErrorComponent):
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
        from ..models.api_v1_condition_instances_update_active_error_component import (
            ApiV1ConditionInstancesUpdateActiveErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_annotations_error_component import (
            ApiV1ConditionInstancesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_archived_at_error_component import (
            ApiV1ConditionInstancesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_archived_error_component import (
            ApiV1ConditionInstancesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_archived_reason_error_component import (
            ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_condition_error_component import (
            ApiV1ConditionInstancesUpdateConditionErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_context_error_component import (
            ApiV1ConditionInstancesUpdateContextErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_criticality_error_component import (
            ApiV1ConditionInstancesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_debug_mode_error_component import (
            ApiV1ConditionInstancesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_display_name_error_component import (
            ApiV1ConditionInstancesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_immediate_error_component import (
            ApiV1ConditionInstancesUpdateImmediateErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_kind_error_component import (
            ApiV1ConditionInstancesUpdateKindErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_labels_error_component import (
            ApiV1ConditionInstancesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_name_error_component import (
            ApiV1ConditionInstancesUpdateNameErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_non_field_errors_error_component import (
            ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_object_id_error_component import (
            ApiV1ConditionInstancesUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_platform_service_error_component import (
            ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_provider_error_component import (
            ApiV1ConditionInstancesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_provider_id_error_component import (
            ApiV1ConditionInstancesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_provider_reference_error_component import (
            ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_reason_error_component import (
            ApiV1ConditionInstancesUpdateReasonErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_reconciliation_enabled_error_component import (
            ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_resolved_at_error_component import (
            ApiV1ConditionInstancesUpdateResolvedAtErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_sla_availability_error_component import (
            ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_sla_target_error_component import (
            ApiV1ConditionInstancesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_slo_availability_error_component import (
            ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_slo_target_error_component import (
            ApiV1ConditionInstancesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_target_availability_error_component import (
            ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_condition_instances_update_tolerations_error_component import (
            ApiV1ConditionInstancesUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ConditionInstancesUpdateActiveErrorComponent
                | ApiV1ConditionInstancesUpdateAnnotationsErrorComponent
                | ApiV1ConditionInstancesUpdateArchivedAtErrorComponent
                | ApiV1ConditionInstancesUpdateArchivedErrorComponent
                | ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent
                | ApiV1ConditionInstancesUpdateConditionErrorComponent
                | ApiV1ConditionInstancesUpdateContextErrorComponent
                | ApiV1ConditionInstancesUpdateCriticalityErrorComponent
                | ApiV1ConditionInstancesUpdateDebugModeErrorComponent
                | ApiV1ConditionInstancesUpdateDisplayNameErrorComponent
                | ApiV1ConditionInstancesUpdateImmediateErrorComponent
                | ApiV1ConditionInstancesUpdateKindErrorComponent
                | ApiV1ConditionInstancesUpdateLabelsErrorComponent
                | ApiV1ConditionInstancesUpdateNameErrorComponent
                | ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent
                | ApiV1ConditionInstancesUpdateObjectIdErrorComponent
                | ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent
                | ApiV1ConditionInstancesUpdateProviderErrorComponent
                | ApiV1ConditionInstancesUpdateProviderIdErrorComponent
                | ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent
                | ApiV1ConditionInstancesUpdateReasonErrorComponent
                | ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent
                | ApiV1ConditionInstancesUpdateResolvedAtErrorComponent
                | ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent
                | ApiV1ConditionInstancesUpdateSlaTargetErrorComponent
                | ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent
                | ApiV1ConditionInstancesUpdateSloTargetErrorComponent
                | ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent
                | ApiV1ConditionInstancesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_0 = (
                        ApiV1ConditionInstancesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_1 = (
                        ApiV1ConditionInstancesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_2 = (
                        ApiV1ConditionInstancesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_3 = (
                        ApiV1ConditionInstancesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_4 = (
                        ApiV1ConditionInstancesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_5 = (
                        ApiV1ConditionInstancesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_6 = (
                        ApiV1ConditionInstancesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_7 = (
                        ApiV1ConditionInstancesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_8 = (
                        ApiV1ConditionInstancesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_9 = (
                        ApiV1ConditionInstancesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_10 = (
                        ApiV1ConditionInstancesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_11 = (
                        ApiV1ConditionInstancesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_12 = (
                        ApiV1ConditionInstancesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_13 = (
                        ApiV1ConditionInstancesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_14 = (
                        ApiV1ConditionInstancesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_15 = (
                        ApiV1ConditionInstancesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_16 = (
                        ApiV1ConditionInstancesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_17 = (
                        ApiV1ConditionInstancesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_18 = (
                        ApiV1ConditionInstancesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_19 = (
                        ApiV1ConditionInstancesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_20 = (
                        ApiV1ConditionInstancesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_21 = (
                        ApiV1ConditionInstancesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_22 = (
                        ApiV1ConditionInstancesUpdateConditionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_23 = (
                        ApiV1ConditionInstancesUpdateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_24 = (
                        ApiV1ConditionInstancesUpdateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_25 = (
                        ApiV1ConditionInstancesUpdateContextErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_26 = (
                        ApiV1ConditionInstancesUpdateImmediateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_condition_instances_update_error_type_27 = (
                        ApiV1ConditionInstancesUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_condition_instances_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_condition_instances_update_error_type_28 = (
                    ApiV1ConditionInstancesUpdateResolvedAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_condition_instances_update_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_condition_instances_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_condition_instances_update_validation_error.additional_properties = d
        return api_v1_condition_instances_update_validation_error

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
